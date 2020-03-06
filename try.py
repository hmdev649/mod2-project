{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import pandasql as ps\n",
    "import numpy as np\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "import statsmodels.api as sm\n",
    "from statsmodels.formula.api import ols\n",
    "from statsmodels.stats.diagnostic import linear_rainbow, het_breuschpagan\n",
    "from statsmodels.stats.outliers_influence import variance_inflation_factor\n",
    "from statsmodels.stats.stattools import jarque_bera\n",
    "\n",
    "from sklearn.preprocessing import OneHotEncoder\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "\n",
    "\n",
    "import geopandas as gpd\n",
    "\n",
    "# 2019 Sales\n",
    "dfAll = pd.read_csv(\"../../references/dfAll.csv\")\n",
    "\n",
    "# Taking only Single Family Residences between 50000 and 1000000 \n",
    "# As well as taking 5 outliers above 8000 sqft of total living space\n",
    "q2 = (\"\"\"\n",
    "SELECT * \n",
    "FROM dfAll\n",
    "WHERE PropertyType = 11 and SalePrice > 50000 and SalePrice < 10000000 and SqFtTotLiving < 8000\n",
    "\"\"\")\n",
    "dfAll2 = ps.sqldf(q2)\n",
    "\n",
    "# Selecting out factors we are using\n",
    "pvc_df = dfAll2[['SalePrice','ZipCode','SqFtTotLiving']]\n",
    "pvc_df.dropna(inplace=True)\n",
    "\n",
    "# Cleaning ZipCode column so that all zip codes are formatted the same\n",
    "pvc_df['ZipCode'] = pvc_df['ZipCode'].str.split('-').str[0]\n",
    "pvc_df['ZipCode'] = pvc_df['ZipCode'].astype(float)\n",
    "pvc_df['ZipCode'] = pvc_df['ZipCode'].astype(str)\n",
    "pvc_df['ZipCode'] = pvc_df['ZipCode'].str.split('.').str[0]\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "hp-env",
   "language": "python",
   "name": "hp-env"
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
   "version": "3.8.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
