from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.generics import RetrieveUpdateAPIView
import json
import requests
from models import *
from datetime import timedelta, date, datetime
from radii import *

class upload_data(GenericAPIView):
    def post(self, request, format = None):
        data = request.data
        mac = data['mac']
        raspi_id = data['raspi_ID']
        sig = data['signal']
        dev = device.objects.get_or_create(mac_ID = mac)
        raspi = raspi.objects.get(raspi_ID = raspi_id)
        fm = frame.objects.get_or_create(dev = dev, raspi = raspi)
        fm.signal = 1.0/(10.0**(float(sig)/10.0))**0.5
        fm.save()
        frames = frame.objects.filter(dev = dev)
        if raspi_id==5 and len(frames)==len(raspi.objects.all()):
            pos_list = []
            max_sig = 0.0
            for frm in frames:
                pos_list.append([frm.raspi.pos_x,frm.raspi.pos_y,frm.signal])
                if frm.signal>max_sig:
                    max_sig=frm.signal
            final_pos = []
            for i in pos_list:
                final_pos.append([i[0],i[1],i[2]/max_sig])
            x, y = findLocation(final_pos)
            dev.pos_x = x
            dev.pos_y = y
            dev.save()

class setRaspiPos(GenericAPIView):
    def post(self, request, format = None):
        data = request.data
        raspi_id = data['raspi_ID']
        x = data['x']
        y = data['y']
        rasp = raspi.objects.get_or_create(raspi_ID = raspi_id)
        rasp.pos_x = x
        rasp.pos_y = y
        rasp.save()
        return Response({'Result':'Success'})

class getpositions(GenericAPIView):
    def post(self,request,format):
        out = []
        for dev in device.objects.all():
            f = dict()
            f['pos_x'] = dev.pos_x
            f['pos_y'] = dev.pos_y
            f['mac'] = dev.mac_ID
            out.append(f)
        return Response(out)


