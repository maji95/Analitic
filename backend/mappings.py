# Сопоставление названий кнопок с именами таблиц
TABLE_MAPPING = {
    "Angio": "angio_total_2024",
    "Angio_Insurance": "angio_total_2024_insurance",
    "Check UP": "checkup_total_2024",
    "Chirurgie general": "chirurgie_general_total_2024",
    "Chirurgie": "chirurgie_total_2024",
    "Consultations": "consultations_total_2024",
    "ECO CG": "eco_cg_total_2024",
    "Endo-colonoscopie": "endo_colonoscopie_total_2024",
    "Ginecologie": "ginecologie_total_2024",
    "Nastere": "nastere_total_2024",
    "Oftalmologie": "oftalmologie_total_2024",
    "Oftalmologie_Insurance": "oftalmologie_total_2024_insurance",
    "Pediatrie": "pediatrie_total_2024",
    "Radiologie-TC-IRM": "radiologie_ct_mri_total_2024",
    "Imagistica medicala": "radiologie_imagistica_medicala_total_2024",
    "Total": "total_2024",
    "Traumatologie": "traumatologie_total_2024",
    "Traumatologie_Insurance": "traumatologie_total_2024_insurance",
    "USG-specialists": "usg_specialists_total_2024",
    "USG": "usg_total_2024"
}


COLUMN_MAPPING = {

    "Oftalmologie_Insurance": {
        "doctor_name": "doctor_name"
    },
    "Traumatologie_Insurance": {
        "doctor_name": "doctor_name"
    },
    "Traumatologie": {
        "doctor_name": "doctor_group"
    },
    "Oftalmologie": {
        "doctor_name": "doctor_group"
    },
    "Check UP": {
        "doctor_name": "service_name"
    },
    "Endo-colonoscopie": {
        "doctor_name": "group_name"
    },
    "Radiologie-TC-IRM": {
        "doctor_name": "group_name"
    },
    "Total": {
        "doctor_name": "category"
    },

    "Angio_Insurance": {
        "doctor_name": "doctor_program"  # Используем doctor_program
    },
    "Angio": {
        "doctor_name": "doctor_name"
    }
}