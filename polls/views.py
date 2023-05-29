from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import json
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from .serializers import Linkedindataserializers
from .models import Linkedindata

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework import serializers

import json
import requests

def index(request):
    domain = request.get_host()
    return HttpResponse("Hello World"+domain)
#linked in imports
import csv
import requests
from bs4 import BeautifulSoup
import random
# addig nan in data frame while facing value error
import pandas as pd
import numpy as np
#path
dotpath = './media/linkedin/'
# dotpath = './media/linkedin/'
#useragents
user_agent_list =['Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.0 Safari/532.0', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.2 Safari/532.0', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.212.0 Safari/532.0', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.0 Safari/532.1', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.1 Safari/532.1', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.3 Safari/532.1', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.3 Safari/532.2', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.7 Safari/532.2', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.1 Safari/532.2', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.4 Safari/532.2', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.5 Safari/532.2', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.6 Safari/532.2', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.2 Safari/532.2', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Comodo_Dragon/4.1.1.11 Chrome/4.1.249.1042 Safari/532.5', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Iron/4.0.275.2 Chrome/4.0.275.2 Safari/532.8', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.308.0 Safari/532.9', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.1', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.1 Safari/533.2', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.3 Safari/533.2', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Arora/0.11.0 Safari/533.3', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.353.0 Safari/533.3', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.354.0 Safari/533.3', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.358.0 Safari/533.3', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.368.0 Safari/533.4', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.99 Safari/533.4', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.417.0 Safari/534.1', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.427.0 Safari/534.1', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.544.0 Safari/534.10', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.200 Safari/534.10', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Ubuntu/10.10 Chromium/8.0.552.237 Chrome/8.0.552.237 Safari/534.10', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.107 Safari/534.13 v1333515017.9196', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Ubuntu/10.04 Chromium/9.0.595.0 Chrome/9.0.595.0 Safari/534.13', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Ubuntu/10.10 Chromium/9.0.600.0 Chrome/9.0.600.0 Safari/534.14', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.11 Safari/534.16', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.127 Safari/534.16', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.82 Safari/534.16', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Iron/10.0.650.0 Chrome/10.0.650.0 Safari/534.16', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Iron/10.0.650.1 Chrome/10.0.650.1 Safari/534.16', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.642.0 Chrome/10.0.642.0 Safari/534.16', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.648.0 Chrome/10.0.648.0 Safari/534.16', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.648.127 Chrome/10.0.648.127 Safari/534.16', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.648.133 Chrome/10.0.648.133 Safari/534.16', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 SUSE/10.0.626.0 (KHTML, like Gecko) Chrome/10.0.626.0 Safari/534.16', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.458.1 Safari/534.3', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.470.0 Safari/534.3', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Epiphany/2.30.6 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Iron/7.0.520.0 Chrome/7.0.520.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/8.1.0.0 Safari/540.0', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML,like Gecko) Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) Gecko Firefox/3.0.8', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.7.10) Gecko/20050724 Firefox/1.0.6', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.7.12) Gecko/20050922 Fedora/1.0.7-1.1.fc4 Firefox/1.0.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.7.12) Gecko/20051127 Firefox/1.0.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.7.12) Gecko/20051218 Firefox/1.0.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.7.12) Gecko/20060202 CentOS/1.0.7-1.4.3.centos4 Firefox/1.0.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.7.6) Gecko/20050405 Firefox/1.0 (Ubuntu package 1.0.2)', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.7.8) Gecko/20050511 Firefox/1.0.4', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8) Gecko/20051201 Firefox/1.5', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8) Gecko/20051212 Firefox/1.5', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.0.1) Gecko/20060313 Fedora/1.5.0.1-9 Firefox/1.5.0.1 pango-text', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.0.10) Gecko/20070409 CentOS/1.5.0.10-2.el5.centos Firefox/1.5.0.10', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.0.12) Gecko/20070530 Fedora/1.5.0.12-1.fc6 Firefox/1.5.0.12', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.0.12) Gecko/20070718 Red Hat/1.5.0.12-3.el5 Firefox/1.5.0.12', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.0.12) Gecko/20080419 CentOS/1.5.0.12-0.15.el4.centos Firefox/1.5.0.12 pango-text']

class linkedinlistview(ListCreateAPIView):
    queryset = Linkedindata.objects.all()
    serializer_class = Linkedindataserializers

class linkedindeleteview(RetrieveUpdateDestroyAPIView):
    queryset = Linkedindata.objects.all()
    serializer_class = Linkedindataserializers



class LinkedinapiView(ListCreateAPIView):
    serializer_class = Linkedindataserializers
    queryset = Linkedindata.objects.all()

    def post(self, request):
        input_url = request.data.get('inputlink')
        if not input_url:
            input_url = request.query_params.get('inputlink')
        
        try:
            for i in range(1,2):
                #Pick a random user agent
                user_agent = random.choice(user_agent_list)
                headers = {'User-Agent': user_agent }
                print(user_agent)
            response = requests.get(input_url, headers = headers)
            print(response)
            soup = BeautifulSoup(response.content,'html.parser')
            main_div=soup.find_all("div",class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card")
            # articles=main_div.find_all("div",class_="articles")
            joblink = []
            for i in main_div:
                #b = i.find('a').get('href')'
                b= i.find('a')
                joblink.append(b.attrs['href'])
            # print(joblink)
            print(len(joblink))
            d=soup.find_all('div', class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card")

            jobs_name = []

            for title in d:
                jobs_name.append(title.text.strip())
            
            # print(jobs_name)
            print(len(jobs_name))
            basedata = {'Jobname': jobs_name, 'Joblink': joblink,}

            basedf = pd.DataFrame(data=basedata)
            #display(df.head())
            basefile = dotpath+'basedata.csv'
            basedf.to_csv(basefile, index=False)

            dataframereading = pd.read_csv(basefile)
            # linkslist = dataframereading['Joblink']
            linkslist = dataframereading['Joblink'].str.strip().values.tolist()
            #jobs_description = []
            jobs_details = []
            # jobs_name =[]
            for link in linkslist:
                #print(link)
                #url = 'https://www.linkedin.com/jobs/view/python-developer-at-donato-technologies-inc-3534800375?refId=XE%2FYwGrdxktzP56hrgM1qQ%3D%3D&trackingId=MJ%2BEe6RIYRul1XLOEKU7yw%3D%3D&position=2&pageNum=0&trk=public_jobs_jserp-result_search-card'
                response = requests.get(link, headers = headers)
                #print(response)
                soup = BeautifulSoup(response.content,'html.parser')
                jobupdate=soup.find_all('div', class_="show-more-less-html__markup")

                #jobs_details = []
                for title in jobupdate:
                    jobs_details.append(title.text.strip())

        
                # print(jobs_details)
                # print(len(jobs_details))
                # jobs_description.append(jobs_details)
                # print(jobs_description)
            linkeindataset = {'Jobsdescriptions': jobs_details,}
            linkeindatasetdfs = pd.DataFrame(data=linkeindataset)
            # display(dfs.head())
            linkedindatafile = dotpath+'linkedindata.csv'
            linkeindatasetdfs.to_csv(linkedindatafile, index=False)
                        
            # reading csv file
            dataframes = pd.read_csv(linkedindatafile)

            # filtering the rows where Credit-Rating contains an email address or phone number
            dataframes = dataframes[dataframes['Jobsdescriptions'].str.contains(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b|\b\d{3}[-.]?\d{3}[-.]?\d{4}\b')]
            # print(dataframes)
            linkedinoutputdatafile = dotpath+'linkedinoutput.csv'
            dataframes.to_csv(linkedinoutputdatafile, index=False)
            jobdataset = pd.read_csv(linkedinoutputdatafile)
            jobsdata = jobdataset['Jobsdescriptions'].str.strip().values.tolist()
            # jobsdata
            ## saving in to database  
            #overallseo = Sitemapapi.objects.create(xmls=input_url, brokenlinks=broken_data, workinglinks=working_data)
            # print(output_data)
            # serializer = PageperformanceSerializer(seo)
            #serializer = SitemapapiSerializer(overallseo)
            #return Response(serializer.data)
            domain = request.get_host()
            ## not saving into database
            file_paths = '/media/linkedin/linkedinoutput.csv'
            file_url = f"http://{domain}{file_paths}"
            data = {
            "inputlink": input_url,
            "filtereddata": jobsdata,
            "outputcsv": file_url,
            }
            return Response(data)
                
        except requests.exceptions.HTTPError as http_err:
            # Return an error response with the URL and error message
            error_msg = f"HTTP error occurred: {http_err}"
            error_data = {'url': input_url, 'error': error_msg}
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            # Return an error response with the URL and error message
            error_msg = f"An error occurred: {err}"
            error_data = {'url': input_url, 'error': error_msg}
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)