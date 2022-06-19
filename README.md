# surfs_up

### Purpose 
The purpose of the challenge / module was to get the temperature statistics during Summer & Winter seasons in Oahu. W. Avy likes our analysis, but he wants more information to find the trends before opening the surf shopso as to determine if the surf and ice cream shop business is sustainable year-round. For analysis we used SQLAlchemy to query SQLite Database.

### Resources 
- Data Source 
  - hawaii.sqlite
- Software 
  - Python 3.8.5, 
  - Jupiter Notebook 6.1.4

### Results 
The Mean temperature in June(74F) is higher than that of Decemeber (71F) while the minimum & maximum temperature are more or less comparable.
Temperature Statistics for June

![image](https://user-images.githubusercontent.com/98556229/174460576-eef851b2-9440-4d61-9915-219b21fac692.png)

histogram plotting for June 

![image](https://user-images.githubusercontent.com/98556229/174462773-7f796a61-b50b-410a-88d9-be19ed35f482.png)


Temperature Statistics for December

![image](https://user-images.githubusercontent.com/98556229/174460583-735df588-323c-48b4-8169-c4b03e0ca19b.png)

histogram plotting for December

![image](https://user-images.githubusercontent.com/98556229/174462782-79731dcf-5a89-4aa6-89c1-6ea75a05a13d.png)


For additional queries - 
For the give data a new dataframe for June & December with Temperatures and Precipitation is created. And scatter plot analysis with linear regression is carried out. 

June Stats, Scatter plot and  linear regression.

![image](https://user-images.githubusercontent.com/98556229/174463022-cf04c84e-f1d6-43c8-bc33-8420a0851070.png)
![image](https://user-images.githubusercontent.com/98556229/174463038-ecb1006e-f8fb-439d-8d3a-338de3dac0eb.png)


December Stats, Scatter plot and  linear regression.
![image](https://user-images.githubusercontent.com/98556229/174463047-ba82f599-87da-444f-bcfd-73980b7ab6f6.png)
![image](https://user-images.githubusercontent.com/98556229/174463051-41af15fd-153e-4ddc-bbb8-a00266d0f9f3.png)

June (slope = -.04) has a slightly steeper slope than December (slope = -.02), which shows that as the temperature increases the precipation slightly decreases in June compared to December. However, the difference is very minimal.From the plots we can see that in June there two-three outliers abover 3inches while in December there are quite a few outliers over 3inches. 

### Conclusion 
The data shows that we can have a Surfing & Ice-cream store in Oahu , in both the seasons.


