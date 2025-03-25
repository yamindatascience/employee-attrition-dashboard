{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0c0b6d86-eec9-47b5-bec1-78a2ea16a882",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (1.44.0)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (5.5.0)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (1.9.0)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (5.5.2)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: numpy<3,>=1.23 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<25,>=20 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (24.0)\n",
      "Requirement already satisfied: pandas<3,>=1.4.0 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (2.2.2)\n",
      "Requirement already satisfied: pillow<12,>=7.1.0 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (10.3.0)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (5.29.2)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (19.0.1)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (2.31.0)\n",
      "Requirement already satisfied: tenacity<10,>=8.1.0 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (9.0.0)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.4.0 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (4.12.2)\n",
      "Requirement already satisfied: watchdog<7,>=2.1.5 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (6.0.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (3.1.44)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (0.9.1)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (6.4)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.3)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.21.1)\n",
      "Requirement already satisfied: narwhals>=1.14.2 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from altair<6,>=4.0->streamlit) (1.32.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.6)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.2.1)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2024.2.2)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.5)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.2.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.34.0)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\yghowrwa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.16.0)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 24.0 -> 25.0.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7efe0c62-a0b1-4068-b807-d8535287f82e",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-03-25 16:36:26.197 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:26.198 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:26.280 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\yghowrwa\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-03-25 16:36:26.282 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:26.284 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:26.285 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:26.286 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:26.286 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:26.287 Session state does not function when running a script without `streamlit run`\n",
      "2025-03-25 16:36:26.288 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:26.288 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:26.290 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:26.397 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:26.625 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:26.626 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:26.627 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:26.704 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:26.900 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:26.902 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:26.902 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:26.957 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:27.183 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:27.184 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:27.184 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:27.333 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:27.641 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:27.642 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:27.643 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:27.717 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:27.945 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:27.947 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:27.948 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:28.051 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:28.297 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:28.298 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:28.300 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:28.383 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:28.890 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-25 16:36:28.891 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Load dataset\n",
    "df = pd.read_csv(\"WA_Fn-UseC_-HR-Employee-Attrition.csv\")\n",
    "\n",
    "st.set_page_config(page_title=\"Employee Attrition Dashboard\", layout=\"wide\")\n",
    "\n",
    "st.title(\"📊 Employee Attrition Dashboard\")\n",
    "\n",
    "# Sidebar - Gender Filter\n",
    "genders = df['Gender'].unique()\n",
    "selected_gender = st.sidebar.selectbox(\"Select Gender\", options=['All'] + list(genders))\n",
    "filtered_df = df if selected_gender == 'All' else df[df['Gender'] == selected_gender]\n",
    "\n",
    "# Define chart plotters\n",
    "def plot_chart(fig_func):\n",
    "    fig = fig_func()\n",
    "    st.pyplot(fig)\n",
    "\n",
    "def job_satisfaction_chart():\n",
    "    fig, ax = plt.subplots()\n",
    "    sns.countplot(data=filtered_df, x='JobSatisfaction', hue='Attrition', ax=ax)\n",
    "    ax.set_title(\"Attrition by Job Satisfaction Level\")\n",
    "    return fig\n",
    "\n",
    "def job_level_chart():\n",
    "    fig, ax = plt.subplots()\n",
    "    sns.countplot(data=filtered_df, x='JobLevel', hue='Attrition', ax=ax)\n",
    "    ax.set_title(\"Attrition by Job Level\")\n",
    "    return fig\n",
    "\n",
    "def income_boxplot():\n",
    "    fig, ax = plt.subplots()\n",
    "    sns.boxplot(data=filtered_df, x='Attrition', y='MonthlyIncome', ax=ax)\n",
    "    ax.set_title(\"Monthly Income Distribution by Attrition Status\")\n",
    "    return fig\n",
    "\n",
    "def years_current_role_chart():\n",
    "    fig, ax = plt.subplots()\n",
    "    sns.histplot(data=filtered_df, x='YearsInCurrentRole', hue='Attrition', kde=True, multiple='stack', ax=ax)\n",
    "    ax.set_title(\"Attrition by Years in Current Role\")\n",
    "    return fig\n",
    "\n",
    "def age_distribution_chart():\n",
    "    fig, ax = plt.subplots()\n",
    "    sns.kdeplot(data=filtered_df, x='Age', hue='Attrition', fill=True, common_norm=False, ax=ax)\n",
    "    ax.set_title(\"Age Distribution of Employees by Attrition Status\")\n",
    "    return fig\n",
    "\n",
    "def distance_chart():\n",
    "    fig, ax = plt.subplots()\n",
    "    sns.histplot(data=filtered_df, x='DistanceFromHome', hue='Attrition', kde=True, multiple='stack', ax=ax)\n",
    "    ax.set_title(\"Attrition by Distance From Home\")\n",
    "    return fig\n",
    "\n",
    "def job_role_chart():\n",
    "    fig, ax = plt.subplots(figsize=(10, 5))\n",
    "    sns.countplot(data=filtered_df, x='JobRole', hue='Attrition', ax=ax)\n",
    "    ax.set_title(\"Attrition Count by Job Role\")\n",
    "    plt.xticks(rotation=45)\n",
    "    return fig\n",
    "\n",
    "# Display charts in expanders\n",
    "with st.expander(\"📌 Attrition by Job Satisfaction\"):\n",
    "    plot_chart(job_satisfaction_chart)\n",
    "\n",
    "with st.expander(\"📌 Attrition by Job Level\"):\n",
    "    plot_chart(job_level_chart)\n",
    "\n",
    "with st.expander(\"📌 Monthly Income by Attrition\"):\n",
    "    plot_chart(income_boxplot)\n",
    "\n",
    "with st.expander(\"📌 Attrition by Years in Current Role\"):\n",
    "    plot_chart(years_current_role_chart)\n",
    "\n",
    "with st.expander(\"📌 Age Distribution by Attrition\"):\n",
    "    plot_chart(age_distribution_chart)\n",
    "\n",
    "with st.expander(\"📌 Attrition by Distance From Home\"):\n",
    "    plot_chart(distance_chart)\n",
    "\n",
    "with st.expander(\"📌 Attrition by Job Role\"):\n",
    "    plot_chart(job_role_chart)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d21693b3-a283-4243-91d6-179f3049c804",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "03292e7a-3b08-4626-9aa4-6d9154b7982b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "10b21490-46ce-4ba9-80ae-8856a25e3bed",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b2236c78-1dc0-4d89-a1ef-9a48255f1272",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c621cac-d2b7-48ba-baf1-3b431e2eae71",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ed81160-85bb-41e4-8695-23faf7f82af4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f29ad57e-8eca-4ad3-9017-353e0f747709",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b188dcc3-98de-4fe0-b861-22a4d1334fdc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
