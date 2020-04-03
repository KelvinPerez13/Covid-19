from selenium import webdriver
from parsel import Selector
from time import sleep
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time
import csv
from datetime import datetime

app = QtWidgets.QApplication([])
dlg = uic.loadUi("UI/dashboard.ui")
dlg2 = uic.loadUi("UI/india.ui")
dlg3 = uic.loadUi("UI/world.ui")


def world():
    try:
        chromedrivers = r'C:\Users\DELL\.PyCharm2019.2\config\scratches\CoronaStatistics\chromedriver2'  # Change the path according to your requirement
        driver_new = webdriver.Chrome(executable_path=chromedrivers)
        QApplication.processEvents()
        driver_new.set_window_position(-10000, 0)
        QApplication.processEvents()
        driver_new.get("https://infographics.channelnewsasia.com/covid-19/map.html")
        dlg3.dot_lbl.setText(".")
        QApplication.processEvents()
        sleep(4)
        dlg3.dot_lbl.setText(". .")
        QApplication.processEvents()
        sel = Selector(text=driver_new.page_source)
        confirmed_cases = sel.xpath('//*[@id="contentcases"]/text()').extract()[0]
        confirmed_cases = confirmed_cases.split()[0]
        reported_deaths = sel.xpath('//*[@id="contentdeaths"]/text()').extract()[0]
        reported_deaths = reported_deaths.split()[0]
        recovered = sel.xpath('//*[@id="contentrec"]/text()').extract()[0]
        recovered = recovered.split()[0]
        last_updated = sel.xpath('//*[@id="updatediv"]/text()').extract()[0]
        last_updated = last_updated.split()[2] + " " + last_updated.split()[3] + " " + last_updated.split()[4]
        QApplication.processEvents()
        dlg3.confirmed_lbl.setText("Total Confirmed Cases:- " + confirmed_cases)
        dlg3.deaths_lbl.setText("Total Reported Deaths:- " + reported_deaths)
        dlg3.recovered_lbl.setText("Total Recovered:- " + recovered)
        dlg3.updated_lbl.setText("Last Updated:- " + last_updated)
        sleep(2)
        dlg3.dot_lbl.setText(". . .")
        QApplication.processEvents()
        driver_new.find_element_by_xpath('//*[@id="dataDivTab"]').click()
        sleep(2)
        dlg3.dot_lbl.setText(". . . .")
        QApplication.processEvents()
        sel = Selector(text=driver_new.page_source)
        countries = sel.xpath('//*[@class="dataDivCol1"]/text()').extract()
        countries.pop(0)
        countries.pop(-1)
        confirm = sel.xpath('//*[@class="dataDivCol2"]/text()').extract()
        confirm.pop(-1)
        death = sel.xpath('//*[@class="dataDivCol3"]/text()').extract()
        death.pop(-1)
        recover = sel.xpath('//*[@class="dataDivCol4"]/text()').extract()
        recover.pop(-1)
        row_number = 0
        for i, j, k, l in zip(countries, confirm, death, recover):
            QApplication.processEvents()
            dlg3.data_tw.insertRow(row_number)
            cell = QtWidgets.QTableWidgetItem(str(i))
            dlg3.data_tw.setItem(row_number, 0, cell)
            cell = QtWidgets.QTableWidgetItem(str(j))
            dlg3.data_tw.setItem(row_number, 1, cell)
            cell = QtWidgets.QTableWidgetItem(str(k))
            dlg3.data_tw.setItem(row_number, 2, cell)
            cell = QtWidgets.QTableWidgetItem(str(l))
            dlg3.data_tw.setItem(row_number, 3, cell)
            QApplication.processEvents()
            row_number += 1
        driver_new.close()
        dlg3.fetching_lbl.hide()
        dlg3.wait_lbl.hide()
        dlg3.dot_lbl.hide()
        dlg3.back_pb.show()
        dlg3.heading_lbl.show()
        dlg3.confirmed_lbl.show()
        dlg3.deaths_lbl.show()
        dlg3.recovered_lbl.show()
        dlg3.updated_lbl.show()
        dlg3.countrywise_lbl.show()
        dlg3.data_tw.show()
        dlg3.info_lbl.show()
        dlg3.save_pb.show()
        dlg3.data_save_lbl.show()
    except Exception as e:
        print(e)


def india():
    try:
        chromedrivers = r'C:\Users\DELL\.PyCharm2019.2\config\scratches\CoronaStatistics\chromedriver2'  # Change the path according to your requirement
        driver_new = webdriver.Chrome(executable_path=chromedrivers)
        QApplication.processEvents()
        driver_new.set_window_position(-10000, 0)
        QApplication.processEvents()
        driver_new.get("https://www.mohfw.gov.in/")
        dlg2.dot_lbl.setText(".")
        QApplication.processEvents()
        sleep(4)
        dlg2.dot_lbl.setText(". .")
        QApplication.processEvents()
        sel = Selector(text=driver_new.page_source)
        active_cases = sel.xpath('//*[@class="bg-blue"]/strong/text()').extract()[0]
        cured = sel.xpath('//*[@class="bg-green"]/strong/text()').extract()[0]
        deaths = sel.xpath('//*[@class="bg-red"]/strong/text()').extract()[0]
        migrated = sel.xpath('//*[@class="bg-orange"]/strong/text()').extract()[0]
        last_updated = sel.xpath('//*[@class="status-update"]/h2/span/text()').extract()[0]
        last_updated = last_updated.split(':')[1] + ":" + last_updated.split(':')[2] + ":" + last_updated.split(':')[3]
        last_updated = last_updated.strip()
        confirmed_cases = str(int(active_cases) + int(cured) + int(deaths) + int(migrated))
        total_cured = str(int(cured) + int(migrated))
        QApplication.processEvents()
        dlg2.confirmed_lbl.setText("Total Confirmed Cases:- " + confirmed_cases)
        dlg2.deaths_lbl.setText("Total Reported Deaths:- " + deaths)
        dlg2.recovered_lbl.setText("Total Recovered:- " + total_cured)
        dlg2.updated_lbl.setText("Last Updated:- " + last_updated)
        sleep(2)
        dlg2.dot_lbl.setText(". . .")
        QApplication.processEvents()
        driver_new.find_element_by_xpath('//*[@class="open-table"]').click()
        sleep(2)
        dlg2.dot_lbl.setText(". . . .")
        QApplication.processEvents()
        sel = Selector(text=driver_new.page_source)
        main_lst = sel.xpath('//*[@class="table table-striped"]/tbody/tr/td/text()').extract()
        del main_lst[-4:]
        states = []
        confirm = []
        death = []
        recover = []
        for i in range(1, len(main_lst), 5):
            states.append(main_lst[i])
        for i in range(2, len(main_lst), 5):
            confirm.append(main_lst[i])
        for i in range(3, len(main_lst), 5):
            recover.append(main_lst[i])
        for i in range(4, len(main_lst), 5):
            death.append(main_lst[i])
        row_number = 0
        for i, j, k, l in zip(states, confirm, death, recover):
            QApplication.processEvents()
            dlg2.data_tw.insertRow(row_number)
            cell = QtWidgets.QTableWidgetItem(str(i))
            dlg2.data_tw.setItem(row_number, 0, cell)
            cell = QtWidgets.QTableWidgetItem(str(j))
            dlg2.data_tw.setItem(row_number, 1, cell)
            cell = QtWidgets.QTableWidgetItem(str(k))
            dlg2.data_tw.setItem(row_number, 2, cell)
            cell = QtWidgets.QTableWidgetItem(str(l))
            dlg2.data_tw.setItem(row_number, 3, cell)
            QApplication.processEvents()
            row_number += 1
        driver_new.close()
        dlg2.fetching_lbl.hide()
        dlg2.wait_lbl.hide()
        dlg2.dot_lbl.hide()
        dlg2.back_pb.show()
        dlg2.heading_lbl.show()
        dlg2.confirmed_lbl.show()
        dlg2.deaths_lbl.show()
        dlg2.recovered_lbl.show()
        dlg2.updated_lbl.show()
        dlg2.statewise_lbl.show()
        dlg2.data_tw.show()
        dlg2.save_pb.show()
        dlg2.data_save_lbl.show()
    except Exception as e:
        print(e)


def india_btn():
    dlg2.dot_lbl.clear()
    dlg2.fetching_lbl.show()
    dlg2.wait_lbl.show()
    dlg2.dot_lbl.show()
    dlg2.back_pb.hide()
    dlg2.heading_lbl.hide()
    dlg2.confirmed_lbl.hide()
    dlg2.deaths_lbl.hide()
    dlg2.recovered_lbl.hide()
    dlg2.updated_lbl.hide()
    dlg2.statewise_lbl.hide()
    dlg2.data_tw.hide()
    dlg2.save_pb.hide()
    dlg2.data_save_lbl.hide()
    dlg2.show()
    dlg.close()
    india()


def back():
    dlg2.data_save_lbl.clear()
    dlg.show()
    clearData()
    dlg2.close()


def world_btn():
    dlg3.dot_lbl.clear()
    dlg3.fetching_lbl.show()
    dlg3.wait_lbl.show()
    dlg3.dot_lbl.show()
    dlg3.back_pb.hide()
    dlg3.heading_lbl.hide()
    dlg3.confirmed_lbl.hide()
    dlg3.deaths_lbl.hide()
    dlg3.recovered_lbl.hide()
    dlg3.updated_lbl.hide()
    dlg3.countrywise_lbl.hide()
    dlg3.data_tw.hide()
    dlg3.save_pb.hide()
    dlg3.data_save_lbl.hide()
    dlg3.info_lbl.hide()
    dlg3.show()
    dlg.close()
    world()


def back2():
    dlg3.data_save_lbl.clear()
    dlg.show()
    clearData2()
    dlg3.close()


def clearData():
    dlg2.data_tw.clearSelection()
    while dlg2.data_tw.rowCount() > 0:
        dlg2.data_tw.removeRow(0)
        dlg2.data_tw.clearSelection()


def clearData2():
    dlg3.data_tw.clearSelection()
    while dlg3.data_tw.rowCount() > 0:
        dlg3.data_tw.removeRow(0)
        dlg3.data_tw.clearSelection()


def saveDataIndia():
    date = datetime.now()
    new_date_time = str(date.year) + str(date.month) + str(date.day) + str(date.hour) + str(date.minute) + str(
        date.second)
    writer = csv.writer(open(
        "C:\\Users\DELL\.PyCharm2019.2\config\scratches\CoronaStatistics\SavedFiles\\" + "India_Stats" + new_date_time + '.csv',
        'w', encoding="utf-8", newline=''))  # Change the path according to your requirement
    a = b"State / UT"
    b = b"Confirmed Cases"
    c = b"Reported Deaths"
    d = b"Recovered"
    writer.writerow(
        [a.decode(), b.decode(), c.decode(), d.decode()])
    row = dlg2.data_tw.rowCount()
    try:
        for i in range(row):
            item1 = dlg2.data_tw.item(i, 0)
            state = item1.text()
            item2 = dlg2.data_tw.item(i, 1)
            confirm = item2.text()
            item3 = dlg2.data_tw.item(i, 2)
            death = item3.text()
            item4 = dlg2.data_tw.item(i, 3)
            recover = item4.text()
            writer.writerow([state, confirm, death, recover])
        total_confirm = dlg2.confirmed_lbl.text().split(':-')[1].strip()
        total_death = dlg2.deaths_lbl.text().split(':-')[1].strip()
        total_recover = dlg2.recovered_lbl.text().split(':-')[1].strip()
        last_updated = dlg2.updated_lbl.text()
        writer.writerow(['Total', total_confirm, total_death, total_recover])
        writer.writerow([last_updated, '', '', ''])
        dlg2.data_save_lbl.setText("Data Saved")
    except Exception as e:
        print(e)


def saveDataWorld():
    date = datetime.now()
    new_date_time = str(date.year) + str(date.month) + str(date.day) + str(date.hour) + str(date.minute) + str(
        date.second)
    writer = csv.writer(open(
        "C:\\Users\DELL\.PyCharm2019.2\config\scratches\CoronaStatistics\SavedFiles\\" + "World_Stats" + new_date_time + '.csv',
        'w', encoding="utf-8", newline=''))  # Change the path according to your requirement
    a = b"Country"
    b = b"Confirmed Cases"
    c = b"Reported Deaths"
    d = b"Recovered *"
    writer.writerow(
        [a.decode(), b.decode(), c.decode(), d.decode()])
    row = dlg3.data_tw.rowCount()
    try:
        for i in range(row):
            item1 = dlg3.data_tw.item(i, 0)
            state = item1.text()
            item2 = dlg3.data_tw.item(i, 1)
            confirm = item2.text()
            item3 = dlg3.data_tw.item(i, 2)
            death = item3.text()
            item4 = dlg3.data_tw.item(i, 3)
            recover = item4.text()
            writer.writerow([state, confirm, death, recover])
        total_confirm = dlg3.confirmed_lbl.text().split(':-')[1].strip()
        total_death = dlg3.deaths_lbl.text().split(':-')[1].strip()
        total_recover = dlg3.recovered_lbl.text().split(':-')[1].strip()
        last_updated = dlg3.updated_lbl.text()
        info = dlg3.info_lbl.text()
        writer.writerow(['Total', total_confirm, total_death, total_recover])
        writer.writerow([last_updated, '', '', ''])
        writer.writerow([info, '', '', ''])
        dlg3.data_save_lbl.setText("Data Saved")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    dlg.setWindowIcon(QIcon('Images/covid-19.jpg'))  # Change the path according to your requirement
    dlg2.setWindowIcon(QIcon('Images/covid-19.jpg'))  # Change the path according to your requirement
    dlg3.setWindowIcon(QIcon('Images/covid-19.jpg'))  # Change the path according to your requirement
    splash_pix = QPixmap('Images/covid-19.jpg')  # Change the path according to your requirement
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)
    progressBar = QProgressBar(splash)
    progressBar.setMaximum(10)
    progressBar.setGeometry(0, splash_pix.height() - 50, splash_pix.width(), 20)
    splash.show()
    for i in range(1, 11):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.15:
            app.processEvents()
    dlg.india_pb.pressed.connect(india_btn)
    dlg2.save_pb.pressed.connect(saveDataIndia)
    dlg.world_pb.pressed.connect(world_btn)
    dlg3.save_pb.pressed.connect(saveDataWorld)
    dlg2.back_pb.pressed.connect(back)
    dlg3.back_pb.pressed.connect(back2)
    dlg.show()
    splash.finish(dlg)
    app.exec()
