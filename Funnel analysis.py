import pandas as pd
df = pd.read_csv("Applicant behaviour data.csv")

print(df.head())
## FUnnel analysis is used  to answer question like how many started and how many reach the destination
funnel = df['page_name'].value_counts().reset_index()
funnel.columns = ['page','visits']
funnel
print(funnel)
funnel.to_csv("Final last file",index=False)

#Drop_off analysis
Drop_offs = df[df['event_type'] == 'exit']['page_name'].value_counts()
Drop_offs
print(Drop_offs)
Drop_offs.to_csv("Final last file",index=False)

#Conversion rate calculation
#To calculate the percentage of users who completed the application process
#total_users = df['user_id'].nunique()
#completed_users = df[df['application_stage'] == 'Completed']['user_id'].nunique()

#conversion_rate = (completed_users / total_users) * 100
#conversion_rate
#print(conversion_rate)

##Device wise completion analysis
#device_conversion = df[df['application_stage'] == 'completed']['device_type'].value_counts()
#device_conversion
#print("The percne is:",device_conversion)

##Traffic source completion
#traffic_performance = df[df['application_stage'] == 'Completed']['traffic_source'].value_counts()
#traffic_performance
#print(traffic_performance)













