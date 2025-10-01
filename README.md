# An Explainable AI Model Integrating Radiomics and Dosiomics to Predict Radiation Pneumonitis in Lung Cancer: Development and External Validation in a Bangladeshi Cohort


<p align="center">
  <a href="https://www.linkedin.com/in/s-h-shuvo/">
    <img src="https://img.shields.io/badge/LinkedIn-Shahadat Hossen Shuvo-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn">
  </a>
  <a href="mailto:27shuvo.edu@gmail.com">
    <img src="https://img.shields.io/badge/Email-Contact_Me-red?style=for-the-badge&logo=gmail" alt="Email">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue.svg?style=flat-square" alt="Python 3.10">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License: MIT">
</p>

---
<p text-align='justify'>
  

This repository contains the complete codebase and documentation for my undergraduate thesis at Gono University. The project focuses on developing a robust, explainable AI model to predict the risk of Radiation Pneumonitis (RP) in lung cancer patients undergoing radiotherapy.

The core novelty of this research lies in its rigorous two-stage generalizability analysis:
1.  **Development:** An initial model is trained on a large, public dataset from The Cancer Imaging Archive (TCIA).
2.  **External Validation:** The model is then tested on a unique, real-world cohort of patients from hospitals in Bangladesh to assess its performance and robustness in a new clinical environment.

This work is driven by a commitment to leveraging AI to solve tangible clinical problems and improve patient outcomes in oncology.

</p>

---

<p text-align='justify'>

## 🎯 Project Goal

The primary objective is to build a non-invasive tool that uses standard pre-treatment data (CT scans and radiotherapy plans) to generate a personalized risk score for developing clinically significant (Grade ≥ 2) Radiation Pneumonitis. By identifying high-risk patients *before* treatment begins, this tool could enable clinicians to create safer, more individualized treatment plans.
</p>

--- 


## 🔬 Methodology & Workflow

The project follows a powerful pipeline for medical AI research, integrating multiple data modalities for a comprehensive analysis.

**`Pre-Treatment CT (Radiomics)` + `RT Dose Plan (Dosiomics)` + `Clinical Data` ➔ `Feature Extraction` ➔ `AI Model Training` ➔ `Pneumonitis Risk Score (XAI)`**

1.  **Data Curation:** Two cohorts are used: a public development cohort (`NSCLC-Radiomics` from TCIA) and a local validation cohort (from Ahsania Cancer Hospital, Bangladesh).
2.  **Feature Engineering:**
    * **Radiomics:** High-dimensional features quantifying the texture and morphology of lung tissue are extracted from CT scans using `PyRadiomics`.
    * **Dosiomics:** Features quantifying the 3D radiation dose distribution are extracted from DICOM-RT DOSE files.
3.  **Predictive Modeling:** Both classical machine learning (e.g., Random Forest) and deep learning (MLP in PyTorch) models will be developed and compared.
4.  **Explainable AI (XAI):** The final model's predictions will be interpreted using SHAP (SHapley Additive exPlanations) to identify the specific imaging and dosimetric biomarkers that are most predictive of pneumonitis risk.

---


## 💡 Key Novelty Points

* **Generalizability Analysis:** Directly addresses a major challenge in medical AI by testing a model on a new, geographically and ethnically distinct population.
* **Multi-Modal Integration:** Combines radiomics, dosiomics, and clinical data for a holistic patient assessment.
* **Explainability:** Moves beyond a "black box" prediction to provide transparent, interpretable results that can offer new clinical insights.

---


## 👨‍🔬 Researcher

* **Md Shahadat Hossen Shuvo**
    * Final-Year Undergraduate Student
    * Dept. of Medical Physics & Biomedical Engineering
    * Gono University, Savar, Dhaka.
    * Email: [27shuvo.edu@gmail.com](mailto:27shuvo.edu@gmail.com)
    * LinkedIn: [linkedin.com/in/s-h-shuvo](https://www.linkedin.com/in/s-h-shuvo)

---

## 💻 Project Status :  

![Status: Ongoing](https://img.shields.io/badge/Status-Ongoing-brightgreen.svg)

This is an active research project for my undergraduate thesis, due in December 2025.

---

