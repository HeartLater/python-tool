#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import datetime
import commands
import os


while True:
        while True:
            nowTime = datetime.datetime.now()
            if nowTime.hour == 10 and nowTime.minute == 15:
                print nowTime
                break
        os.mknod("/hehe11111.txt")
        while True:
            nowTime = datetime.datetime.now()
            if nowTime.hour == 10 and nowTime.minute == 16:
                print nowTime
                break
        os.mknod("/hehe22222.txt")
        while True:
            nowTime = datetime.datetime.now()
            if nowTime.hour == 10 and nowTime.minute == 17:
                print nowTime
                break
        os.mknod("/hehe3333.txt")
        break

