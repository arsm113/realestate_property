import streamlit as st
import pandas as pd
import ast
# import plotly.express as px
# import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# import seaborn as sns
import plotly.express as px
import seaborn as sns
# st.set_page_config(layout="wide")
def Analysis_app():
  
  # st.set_page_config(page_title="Plotting Demo",layout="wide")
  st.title('Analytics')
  st.header('Overall Map')
  
  new_df = pd.read_csv('data_viz1.csv')
  df1 = pd.read_csv("gurgaon_properties.csv")
  df = pd.read_csv("gurgaon_properties_missing_value_imputation.csv")
  
  group_df = new_df.groupby('sector')[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']].mean()
  fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                          color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                          mapbox_style="open-street-map", width=1200, height=700, hover_name=group_df.index)
  st.plotly_chart(fig, use_container_width=True)
  
  ## Word cloud
  
  
  wordcloud_df = df1.merge(df, left_index=True, right_index=True)[['features', 'sector']]
  # Select sector
  st.header('WordCloud')
  selected_sector = st.selectbox("Select Sector", ["All"] + wordcloud_df['sector'].unique().tolist())
  
  if selected_sector == 'All':
      main = []
      for item in wordcloud_df['features'].dropna().apply(ast.literal_eval):
          main.extend(item)
      # print(main)
      feature_txt = ' '.join(main)
  
      word_cloud = WordCloud(width=600, height=300,
                             background_color='black',
                             stopwords={'s'},  # Any stopwords you'd like to exclude
                             min_font_size=10).generate(feature_txt)
      st.title(f'Word Cloud for {selected_sector}')
      # st.image(word_cloud.to_array())
      st.set_option('deprecation.showPyplotGlobalUse', False)
      plt.figure(figsize=(10, 4), facecolor=None)
      plt.imshow(word_cloud, interpolation='bilinear')
      plt.axis("off")
      plt.tight_layout(pad=0)
  
      st.pyplot()
  
  else:
  
  
      # Filter DataFrame by selected sector
      filtered_df = wordcloud_df[wordcloud_df['sector'] == selected_sector]
  
      # Extract features
      features_list = filtered_df['features'].explode().dropna().tolist()
      print(features_list)
  
      # Create a Word Cloud
      wordcloud = WordCloud(width=600, height=300, background_color='white').generate(' '.join(features_list))
      st.set_option('deprecation.showPyplotGlobalUse', False)
      plt.figure(figsize=(10, 4), facecolor=None)
      plt.imshow(wordcloud, interpolation='bilinear')
      plt.axis("off")
      plt.tight_layout(pad=0)
  
      st.pyplot()
  
      # Display the Word Cloud
      # st.title(f'Word Cloud for {selected_sector}')
      # st.image(wordcloud.to_array())
  
  # Area vs Price
  
  st.header('Area vs Price')
  property_type = st.selectbox('Select Property Type',['All','House','Flat'])
  if property_type=='All':
      fig1 = px.scatter(new_df, x='built_up_area', y='price', color='bathroom',
                        title='Area vs Price')
      st.plotly_chart(fig1, use_container_width=True)
  elif property_type=='House':
  
      fig1 = px.scatter(new_df[new_df['property_type']=='house'],x='built_up_area',y='price',color='bathroom',title='Area vs Price')
      st.plotly_chart(fig1, use_container_width=True)
  else:
      fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x='built_up_area', y='price', color='bathroom',
                        title='Area vs Price')
      st.plotly_chart(fig1, use_container_width=True)
  
  ## Pie Chart
  st.header('BHK Pie chart')
  
  selected_sector = st.selectbox('Select a Sector',['All']+df['sector'].unique().tolist())
  if selected_sector=='All':
      fig2 = px.pie(df, names='bedRoom', title='Total Bill Amount by Day')
      st.plotly_chart(fig2, use_container_width=True)
  else:
      filtered_data = df[df['sector'] == selected_sector]
      # if filtered_data:
      fig2 = px.pie(filtered_data, names='bedRoom', title='Total Bill Amount by Day')
      st.plotly_chart(fig2, use_container_width=True)
  
  st.header('Side by Side BHK Price Comparison')
  temp_df = df[df['bedRoom'] <= 4]
  selected_sector_box = st.selectbox('Select a Sector',['All']+temp_df['sector'].unique().tolist())
  if selected_sector_box =='All':
      fig3 = px.box(temp_df, x='bedRoom', y='price', title='BHK Price Range')
      st.plotly_chart(fig3, use_container_width=True)
  else:
      filtered_data_box = df[df['sector'] == selected_sector]
      fig4 = px.box(filtered_data_box, x='bedRoom', y='price', title='BHK Price Range')
      st.plotly_chart(fig4, use_container_width=True)
  st.header('Side by side distplot for Property Type')
  sns.set_style(rc = {'axes.facecolor': 'lightsteelblue'})
  fig5 = plt.figure(figsize=(10,4))
  sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
  sns.distplot(new_df[new_df['property_type'] == 'flat']['price'],label='flat')
  plt.legend()
  st.pyplot(fig5)
