import numpy as np
import pandas as pd
from scipy import stats

# Tải .csv vào một khung dữ liệu bằng cách sử dụng read_csv
covid_data = pd.read_csv("baithuchanh\covid19data.csv")
covid_data = covid_data[['code','continent',
'country','date','total_cases','new_cases']]
# lưu tệp data mới vừa được lọc vào covid_data_new
covid_data.to_csv("baithuchanh/covid_data_new.csv", index=False)

# Loại bỏ các dòng có NaN ở cột new_cases
covid_data = covid_data.dropna()


# bước đầu kiểm tra dữ liệu 
covid_data.head(5)
covid_data.dtypes
covid_data.shape

# tính trung bình cột new_cases
data_mean = np.mean(covid_data["new_cases"])

# lấy trung vị của cột new_cases
data_median = np.median(covid_data["new_cases"])

# Get the mode of the data
data_mode = stats.mode(covid_data["new_cases"])

# tính phương sai của cột new_cases
data_variance = np.var(covid_data["new_cases"])

# tính độ lệch chuẩn của cột new_cases 
data_sd = np.std(covid_data["new_cases"])

# Compute the maximum and minimum values of the data
data_max = np.max(covid_data["new_cases"])
data_min = np.min(covid_data["new_cases"])

# lấy giá trị thứ 60 
data_percentile = np.percentile(covid_data["new_cases"],60)

# Obtain the quartiles of the data
data_quartile = np.quantile(covid_data["new_cases"],0.75)

# Get the IQR of the data
data_IQR = stats.iqr(covid_data["new_cases"])

print(" giá trị trung bình: ", data_mean)
print("giá trị trung vị: ", data_median)
print("giá trị mode: ", data_mode)
print("giá trị phương sai: ", data_variance)
print("giá trị độ lệch chuẩn: ", data_sd)  
print("giá trị lớn nhất: ", data_max)
print("giá trị nhỏ nhất: ", data_min)
print("giá trị phần trăm thứ 60: ", data_percentile)
print("giá trị tứ phân vị Q3: ", data_quartile) 
print("giá trị IQR: ", data_IQR)
