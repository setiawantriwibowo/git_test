import pytest
from pages.Home_pages import Home_page
from pages.mstpemilik_pages import MstPemilikPages
from pages.Global_Pages import GlobalPages
import time
from selenium.webdriver.common.by import By
from config import *
from utils.data_test import get_data
from selenium.common.exceptions import ElementNotInteractableException , NoSuchElementException
from utils import data_test
@pytest.mark.mst_pemilik

def test_open_menu(driver):
    mst_pemilik = MstPemilikPages(driver)
    home_page = Home_page(driver)
    home_page.clickButtonMaster()
    home_page.clickButton_MasterPemilik()
    time.sleep(1)
    try :
        result = mst_pemilik.get_title_menu()
        assert "MASTER PEMILIK TOKO" in result
    except NoSuchElementException:
        print("gagal buka menu")

def input_data(driver,name,action):
    all = GlobalPages(driver)
    data = get_data("mst_pemilik",name)
    mst_pemilik = MstPemilikPages(driver)
    time.sleep(1)
    if action == "add_data":
        mst_pemilik.click_tambah_data()
        mst_pemilik.enter_kd_pemilik(data['kd_pemilik'])
    else:
        mst_pemilik.click_btn_dtl()
    mst_pemilik.enter_nm_pemilik(data['nama_pemilik'])
    mst_pemilik.enter_status(data['Status'])
    mst_pemilik.enter_atas_nama(data['Atas_nama'])
    mst_pemilik.enter_no_ktp(data['No_ktp'])
    mst_pemilik.enter_alamat(data['Alamat'])
    mst_pemilik.enter_rt(data['Rt'])
    mst_pemilik.enter_rw(data['Rw'])
    mst_pemilik.enter_kelurahan(data['Kelurahan'])
    mst_pemilik.enter_kecamatan(data['Kec'])
    mst_pemilik.enter_kota(data['kota'])
    mst_pemilik.enter_provinsi(data['Prov'])
    mst_pemilik.enter_kd_pos(data['kd_pos'])
    mst_pemilik.enter_no_telp(data['no_telp'])
    mst_pemilik.enter_fax(data['fax'])
    mst_pemilik.enter_no_hp(data['no_hp'])
    mst_pemilik.enter_email(data['email'])
    mst_pemilik.enter_nama_bank(data['nm_bank'])
    mst_pemilik.enter_cabang_bank(data['cabang_bank'])
    mst_pemilik.enter_an_bank(data['an_bank'])
    mst_pemilik.enter_no_rek(data['no_rek'])
    mst_pemilik.click_PNPKP()
    mst_pemilik.enter_nama_npwp(data['nm_npwp'])
    mst_pemilik.enter_no_npwp(data['no_npwp'])
    mst_pemilik.enter_alamat_npwp(data['alamat_npwp'])
    if action == "add_data":
        mst_pemilik.click_add_detail()
    else:
        mst_pemilik.click_btn_show_dtl()
    mst_pemilik.enter_no_lokasi(data['no_lokasi'])
    mst_pemilik.enter_alamat_lokasi(data['alamat_lokasi'])
    mst_pemilik.click_lov_dc()
    time.sleep(1)
    mst_pemilik.enter_searchbox_dc(data['dc'])
    time.sleep(1)
    mst_pemilik.click_search_dc()
    time.sleep(1)
    mst_pemilik.pilih_dc()
    mst_pemilik.click_lov_kuu()
    mst_pemilik.enter_kuu(data['kuu'])
    mst_pemilik.click_search_kuu()
    mst_pemilik.pilih_kuu()
    mst_pemilik.click_ktp()
    mst_pemilik.enter_ktp(data['ket_ktp'])
    mst_pemilik.click_kk()
    mst_pemilik.enter_kk(data['ket_kk'])
    mst_pemilik.click_siup()
    mst_pemilik.enter_siup(data['ket_siup'])
    mst_pemilik.click_tdp()
    mst_pemilik.enter_tdp(data['ket_tdp'])
    mst_pemilik.click_npwp()
    mst_pemilik.enter_npwp(data['ket_npwp'])
    mst_pemilik.click_domisili()
    mst_pemilik.enter_domisili(data['ket_domisili'])
    mst_pemilik.click_akte()
    mst_pemilik.enter_akte(data['ket_akte'])
    mst_pemilik.click_menkeh()
    mst_pemilik.enter_menkeh(data['ket_menkeh'])
    mst_pemilik.click_proposal()
    mst_pemilik.enter_proposal(data['ket_proposal'])
    mst_pemilik.click_pks()
    mst_pemilik.enter_pks(data['ket_pks'])
    mst_pemilik.click_ho()
    mst_pemilik.enter_ho(data['ket_ho'])
    mst_pemilik.click_situ()
    mst_pemilik.enter_situ(data['ket_situ'])
    mst_pemilik.click_stpuw()
    mst_pemilik.enter_stpuw(data['ket_stpuw'])
    mst_pemilik.click_imb()
    mst_pemilik.enter_imb(data['ket_imb'])
    mst_pemilik.click_it()
    mst_pemilik.enter_it(data['ket_it'])
    time.sleep(1)
    mst_pemilik.click_btn_simpan()
    # try :
    #     all.click_btn_y()
    # except NoSuchElementException :
    #     all.click_batal_add()
    if name == "invalid_add":
        all.click_btn_kembali()
    else :
        all.click_btn_y()

    # if name == "valid_add":
    #     all.click_btn_y()
    # elif name == "inputan_salah":
    #     all.click_btn_y()
    # elif name == "valid_update" :
    #     all.click_btn_y()
    # elif name == "duplicate_add" :
    #     all.click_btn_y()
    time.sleep(5)

def test_tambah_data_valid(driver):
    input_data(driver,"valid_add","add_data")
    driver.refresh()

def test_tambah_data_duplicate(driver):
    all = GlobalPages(driver)
    input_data(driver,"duplicate_add","add_data")
    all.close_duplicate()
    time.sleep(2)
    driver.refresh()

def test_tambah_data_input_salah(driver):
    input_data(driver,"inputan_salah","add_data")
    time.sleep(3)
    driver.refresh()

def test_tambah_data_invalid(driver):
    all =GlobalPages(driver)
    input_data(driver,"invalid_add","add_data")
    time.sleep(2)

def test_hapus(driver):
    all = GlobalPages(driver)
    all.click_btn_hapus()
    all.click_btn_y()
    time.sleep(4)
    driver.refresh()
    
def test_update_data_valid(driver):
    all =GlobalPages(driver)
    input_data(driver,"valid_update","update_data")
    time.sleep(3)
    driver.refresh()
    # time.sleep(3)
    # all.click_btn_kembali()
    # all.click_btn_kembali()
    

def testCobaaaa(driver):
    input_data(driver,"valid_update","update_data")




    
    