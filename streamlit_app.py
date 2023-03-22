# coding=utf-8
import streamlit as st
import matplotlib
import SimpleITK as sitk

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import time
import os
import random


def main():
    st.set_page_config(
        page_title="ProST配准",  # 页面标题
        page_icon=":rainbow:",  # icon
    )
    st.title('ProST配准')
    mod = ''
    if 'mod' not in st.session_state:
        st.session_state['mod'] = '欢迎'
    if st.button('开始配准'):
        st.session_state['mod'] = '开始配准'
    if st.button('开发者信息'):
        st.session_state['mod'] = '开发者信息'
    mod = st.session_state['mod']
    if mod == '欢迎':
        img_ls = os.listdir('assets/img')
        img = random.choice(img_ls)
        image = Image.open('assets/img/' + img)
        st.image(image, caption=img[:img.find('.')])
    if mod == '开始配准':
        with st.form('欢迎光临'):
            ct_file = st.file_uploader('上传CT图像（仅限nii.gz格式）', type=(['nii.gz']))
            if ct_file is not None:
                ct = ct_file.name
                st.write(ct_file)
                # ct_img = sitk.ReadImage(ct)
                # ct_array = sitk.GetArrayFromImage(ct_img)
            x_ray_file = st.file_uploader('上传X光图像（仅限nii.gz格式）', type=(['nii.gz']))
            if x_ray_file is not None:
                x_ray = x_ray_file.name
                st.write(x_ray)
            registration = st.form_submit_button("开始配准")
            if registration:
                st.success('配准成功!', icon="✅")
                st.write('预测参数：[90, 0, 0, 1000, 0, 0]')
                st.image(Image.open('../temp/result.gif'))
        if st.button('返回'):
            st.session_state['mod'] = '欢迎'
            st._rerun()
    if mod == '开发者信息':
        st.markdown('开发者信息')
        if st.button('返回'):
            st.session_state['mod'] = '欢迎'
            st._rerun()
    # if st.button('退出'):
    #     os.system('taskkill /im msedge.exe /F')
    #     os.system('taskkill /im iexplore.exe /F')
    #     os.system('taskkill /im sogouexplorer.exe /F')
    #     os.system('taskkill /im The world .exe /F')
    #     os.system('taskkill /im Firefox.exe /F')
    #     os.system('taskkill /im opera.exe /F')
    #     os.system('taskkill /im 360SE.exe /F')
    #     os.system('taskkill /im Chrome.exe /F')
    #     os.system('taskkill /im Safari.exe /F')
    #     os.system('taskkill /im Maxthon.exe /F')
    #     os.system('taskkill /im Netscape.exe /F')


if __name__ == '__main__':
    main()
