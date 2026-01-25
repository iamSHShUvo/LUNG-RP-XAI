import os
import shutil
import pydicom

def organize_dicom_dataset(source_root, dest_root, move_files=False):
    """
    Organizes DICOM files into the following structure:
    PatientID/
      ├── CT/          (All CT slices)
      ├── STRUCT/      (RT Structure Set file)
      ├── RTPLAN.dcm   (RT Plan file)
      └── RTDOSE.dcm   (RT Dose file)
    """
    
    abs_source = os.path.abspath(source_root)
    abs_dest = os.path.abspath(dest_root)

    print(f"Scanning source: {abs_source}")
    print(f"Destination: {abs_dest}")

    for root, _, files in os.walk(abs_source):
        for filename in files:
            file_path = os.path.join(root, filename)
            
            try:
                # Read DICOM header only (fast)
                ds = pydicom.dcmread(file_path, stop_before_pixels=True)
                
                if 'PatientID' not in ds:
                    print(f"Skipping {filename}: No PatientID found.")
                    continue

                # Sanitize Patient ID for folder creation
                patient_id = str(ds.PatientID).strip()
                safe_patient_id = "".join([c for c in patient_id if c.isalnum() or c in ('-', '_')]).strip()
                
                # Determine Modality
                modality = ds.Modality if 'Modality' in ds else "Unknown"
                
                # Define destination paths based on requirements
                patient_dir = os.path.join(abs_dest, safe_patient_id)
                
                if modality == 'CT':
                    target_dir = os.path.join(patient_dir, 'CT')
                elif modality == 'RTSTRUCT':
                    target_dir = os.path.join(patient_dir, 'STRUCT')
                elif modality in ['RTPLAN', 'RTDOSE']:
                    # Plan and Dose go directly into the main patient folder
                    target_dir = patient_dir
                else:
                    # Other modalities (e.g. PT, MR) go to an 'Other' folder
                    target_dir = os.path.join(patient_dir, 'Other')

                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)

                # Handle duplicate filenames
                dest_path = os.path.join(target_dir, filename)
                base, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(dest_path):
                    dest_path = os.path.join(target_dir, f"{base}_{counter}{ext}")
                    counter += 1

                # Copy or Move
                if move_files:
                    shutil.move(file_path, dest_path)
                else:
                    shutil.copy2(file_path, dest_path)
                
                print(f"[{modality}] {filename} -> {dest_path}")

            except (pydicom.errors.InvalidDicomError, IsADirectoryError):
                continue

if __name__ == "__main__":
    # UPDATE THESE PATHS BEFORE RUNNING
    SOURCE_DIR = r"D:\Thesis_Project\Raw_Data"
    DEST_DIR = r"D:\Thesis_Project\Organized_Data"
    
    # Set to True to move files (delete from source), False to copy
    organize_dicom_dataset(SOURCE_DIR, DEST_DIR, move_files=False)