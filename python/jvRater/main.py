'''
Created on Mar 23, 2013
'''

import sys
from string import split
from os import path
from dict import tagDict

# GUI system
from PyQt4 import QtGui, QtCore, QtXml, uic

class MainWindow(QtGui.QMainWindow):
    def __init__(self): 
        QtGui.QMainWindow.__init__(self)
        
        uic.loadUi(self.buildResPath('jvRater/Main.ui'), self)   # Load window UI
        self.pushButton_make.clicked.connect(self.make)
        self.pushButton_parse.clicked.connect(self.parse)
        self.pushButton_reset.clicked.connect(self.reset)
        
        self.initVars()
        
    def initVars(self):
        self.title = str()
        self.code = str()
        
        self.genre = str()
        self.rating = str()
        
        self.tags = []
        self.series = []
    
    def make(self):
        self.fromOptions()
        
        tagsStr = '(' + self.generateTags(self.tags) + ')'
        seriesStr = self.generateTags(self.series)
        
        if len(seriesStr) > 0: seriesStr = ' ' + seriesStr
        
        codeStr = str()
        if len(self.code) > 0: codeStr= ' [' + self.code + ']'
        
        output = None
        if self.checkBox_tagsOnly.isChecked():
            output = tagsStr
        else:
            output = '%s%s %s - %s%s %s' % (self.genre, seriesStr, self.rating, self.title, codeStr, tagsStr)
            
        self.lineEdit_result.setText(output)
        
    def reset(self):
        self.initVars()
        self.resetAll()
    
    # Make plain text from tags
    def parse(self):
        inputS = str(self.lineEdit_result.text())
        inputS = inputS.strip('()')
        tags = split(inputS.strip('() '), ' ')
        
        output = str()
        
        for x in range(len(tags)):
            tags[x].strip() # remove white spaces
            
        dictS = tagDict
        
        try:
            for x in range(len(tags)):
                if x < len(tags) - 1:
                    output = output + dictS[tags[x]] + ', '
                else:
                    output = output + dictS[tags[x]]
        except KeyError as e:
            print e
        
        if len(output) < 1:
            output = 'No bueno!'
        self.lineEdit_result.setText(output)
    
    def fromOptions(self):
        self.fromBasics()
        self.fromTags()
        self.fromSeries()
    
    def generateTags(self, theList):
        tagList = str()
        for x in range(len(theList)):
            if x < len(theList) - 1:
                tagList = tagList + theList[x] + ' '
            else:
                tagList = tagList + theList[x]  # No space for the last one
                
        return tagList
    
    
    def fromBasics(self):
        self.title = self.lineEdit_title.text()
        self.code = self.lineEdit_code.text()
        
        self.genre = split(self.comboBox_genre.currentText(), ' ')[0]
        self.rating = split(self.comboBox_rating.currentText(), ' ')[0]
    
    def fromTags(self):
        self.tags = []
        
        if self.checkBox_spec_ZZ.isChecked(): self.tags.append('ZZ')
        if self.checkBox_spec_FV.isChecked(): self.tags.append('FV')
        if self.checkBox_spec_HL.isChecked(): self.tags.append('HL')
        if self.checkBox_spec_SE.isChecked(): self.tags.append('SE')
        if self.checkBox_spec_AC.isChecked(): self.tags.append('AC')
        
        if self.checkBox_gen_VY.isChecked(): self.tags.append('VY')
        if self.checkBox_gen_YN.isChecked(): self.tags.append('YN')
        if self.checkBox_gen_MA.isChecked(): self.tags.append('MA')
        if self.checkBox_gen_VD.isChecked(): self.tags.append('VD')
        if self.checkBox_gen_CP.isChecked(): self.tags.append('CP')
        if self.checkBox_gen_CD.isChecked(): self.tags.append('CD')
        if self.checkBox_gen_LE.isChecked(): self.tags.append('LE')
        if self.checkBox_gen_SG.isChecked(): self.tags.append('SG')
        if self.checkBox_gen_ST.isChecked(): self.tags.append('ST')
        if self.checkBox_gen_RL.isChecked(): self.tags.append('RL')
        if self.checkBox_gen_NP.isChecked(): self.tags.append('NP')
        if self.checkBox_gen_LB.isChecked(): self.tags.append('LB')
        if self.checkBox_gen_LO.isChecked(): self.tags.append('LO')
        if self.checkBox_gen_HF.isChecked(): self.tags.append('HF')
        
        if self.checkBox_int_FN.isChecked(): self.tags.append('FN')
        if self.checkBox_int_WD.isChecked(): self.tags.append('WD')
        if self.checkBox_int_BU.isChecked(): self.tags.append('BU')
        if self.checkBox_int_BM.isChecked(): self.tags.append('BM')
        if self.checkBox_int_EM.isChecked(): self.tags.append('EM')
        if self.checkBox_int_TS.isChecked(): self.tags.append('TS')
        if self.checkBox_int_SY.isChecked(): self.tags.append('SY')
        if self.checkBox_int_FA.isChecked(): self.tags.append('FA')
        if self.checkBox_int_GA.isChecked(): self.tags.append('GA')
        if self.checkBox_int_WR.isChecked(): self.tags.append('WR')
        if self.checkBox_int_DR.isChecked(): self.tags.append('DR')
        if self.checkBox_int_DG.isChecked(): self.tags.append('DG')
        if self.checkBox_int_SC.isChecked(): self.tags.append('SC')
        if self.checkBox_int_PB.isChecked(): self.tags.append('PB')
        if self.checkBox_int_SR.isChecked(): self.tags.append('SR')
        if self.checkBox_int_RP.isChecked(): self.tags.append('RP')
        if self.checkBox_int_CO.isChecked(): self.tags.append('CO')
        if self.checkBox_int_OG.isChecked(): self.tags.append('OG')
        if self.checkBox_int_SL.isChecked(): self.tags.append('SL')
        
        if self.checkBox_fet_RA.isChecked(): self.tags.append('RA')
        if self.checkBox_fet_CR.isChecked(): self.tags.append('CR')
        if self.checkBox_fet_LD.isChecked(): self.tags.append('LD')
        if self.checkBox_fet_RC.isChecked(): self.tags.append('RC')
        if self.checkBox_fet_TO.isChecked(): self.tags.append('TO')
        if self.checkBox_fet_TR.isChecked(): self.tags.append('TR')
        if self.checkBox_fet_GR.isChecked(): self.tags.append('GR')
        if self.checkBox_fet_FC.isChecked(): self.tags.append('FC')
        if self.checkBox_fet_HE.isChecked(): self.tags.append('HE')
        if self.checkBox_fet_IS.isChecked(): self.tags.append('IS')
        if self.checkBox_fet_AB.isChecked(): self.tags.append('AB')
        if self.checkBox_fet_PN.isChecked(): self.tags.append('PN')
        if self.checkBox_fet_CH.isChecked(): self.tags.append('CH')
        if self.checkBox_fet_BD.isChecked(): self.tags.append('BD')
        if self.checkBox_fet_FE.isChecked(): self.tags.append('FE')
        if self.checkBox_fet_OR.isChecked(): self.tags.append('OR')
        
        if self.checkBox_gro_SP.isChecked(): self.tags.append('SP')
        if self.checkBox_gro_PE.isChecked(): self.tags.append('PE')
        if self.checkBox_gro_PO.isChecked(): self.tags.append('PO')
        if self.checkBox_gro_VO.isChecked(): self.tags.append('VO')
        
        if self.checkBox_inc_MO.isChecked(): self.tags.append('MO')
        if self.checkBox_inc_FD.isChecked(): self.tags.append('FD')
        if self.checkBox_inc_BS.isChecked(): self.tags.append('BS')
        if self.checkBox_inc_MD.isChecked(): self.tags.append('MD')
        if self.checkBox_inc_FI.isChecked(): self.tags.append('FI')
        if self.checkBox_inc_EF.isChecked(): self.tags.append('EF')
        if self.checkBox_inc_JF.isChecked(): self.tags.append('JF')
        if self.checkBox_inc_RI.isChecked(): self.tags.append('RI')
        if self.checkBox_inc_GI.isChecked(): self.tags.append('GI')
        if self.checkBox_inc_MU.isChecked(): self.tags.append('MU')
        if self.checkBox_inc_FR.isChecked(): self.tags.append('FR')
        if self.checkBox_inc_PR.isChecked(): self.tags.append('PR')
        if self.checkBox_inc_BL.isChecked(): self.tags.append('BL')
        
        if self.checkBox_voy_VR.isChecked(): self.tags.append('VR')
        if self.checkBox_voy_VP.isChecked(): self.tags.append('VP')
        if self.checkBox_voy_VF.isChecked(): self.tags.append('VF')
        if self.checkBox_voy_MB.isChecked(): self.tags.append('MB')
        if self.checkBox_voy_WC.isChecked(): self.tags.append('WC')
        
        if self.checkBox_idl_U14.isChecked(): self.tags.append('U14')
        if self.checkBox_idl_O14.isChecked(): self.tags.append('O14')
        if self.checkBox_idl_AD.isChecked(): self.tags.append('AD')
        
        if self.checkBox_oth_FO.isChecked(): self.tags.append('FO')
        if self.checkBox_oth_QV.isChecked(): self.tags.append('QV')
        if self.checkBox_oth_BQ.isChecked(): self.tags.append('BQ')
        if self.checkBox_oth_UC.isChecked(): self.tags.append('UC')
        if self.checkBox_oth_CL.isChecked(): self.tags.append('CL')
        
        if self.checkBox_girl_GN.isChecked(): self.tags.append('GN')
        if self.checkBox_girl_TN.isChecked(): self.tags.append('TN')
        if self.checkBox_girl_FT.isChecked(): self.tags.append('FT')
        if self.checkBox_girl_MS.isChecked(): self.tags.append('MS')
        if self.checkBox_girl_SK.isChecked(): self.tags.append('SK')
        if self.checkBox_girl_CB.isChecked(): self.tags.append('CB')
        if self.checkBox_girl_DA.isChecked(): self.tags.append('DA')
        if self.checkBox_girl_TI.isChecked(): self.tags.append('TI')
        if self.checkBox_girl_TL.isChecked(): self.tags.append('TL')
        if self.checkBox_girl_BG.isChecked(): self.tags.append('BG')
        if self.checkBox_girl_SH.isChecked(): self.tags.append('SH')
        if self.checkBox_girl_TB.isChecked(): self.tags.append('TB')
        if self.checkBox_girl_CU.isChecked(): self.tags.append('CU')
        if self.checkBox_girl_VI.isChecked(): self.tags.append('VI')
        if self.checkBox_girl_AV.isChecked(): self.tags.append('AV')
        if self.checkBox_girl_CS.isChecked(): self.tags.append('CS')
        if self.checkBox_girl_GF.isChecked(): self.tags.append('GF')
        if self.checkBox_girl_FB.isChecked(): self.tags.append('FB')
    
    def fromSeries(self):
        self.series = []
        if self.checkBox_series_MUS.isChecked(): self.series.append('MUS')
        if self.checkBox_series_BAK.isChecked(): self.series.append('BAK')
        if self.checkBox_series_N24.isChecked(): self.series.append('N24')
        if self.checkBox_series_RRA.isChecked(): self.series.append('RRA')
        if self.checkBox_series_CND.isChecked(): self.series.append('CND')
        if self.checkBox_series_GQU.isChecked(): self.series.append('GQU')
        if self.checkBox_series_RTG.isChecked(): self.series.append('RTG')
        if self.checkBox_series_SPK.isChecked(): self.series.append('SPK')
    
    def resetAll(self):
        self.lineEdit_title.setText('')
        self.lineEdit_code.setText('')
        
        self.comboBox_genre.setCurrentIndex(0)
        self.comboBox_rating.setCurrentIndex(0)
        
        #self.lineEdit_result.setText('')
        
        self.checkBox_spec_ZZ.setChecked(False)
        self.checkBox_spec_FV.setChecked(False)
        self.checkBox_spec_HL.setChecked(False)
        self.checkBox_spec_SE.setChecked(False)
        self.checkBox_spec_AC.setChecked(False)
        
        self.checkBox_gen_VY.setChecked(False)
        self.checkBox_gen_YN.setChecked(False)
        self.checkBox_gen_MA.setChecked(False)
        self.checkBox_gen_VD.setChecked(False)
        self.checkBox_gen_CP.setChecked(False)
        self.checkBox_gen_CD.setChecked(False)
        self.checkBox_gen_LE.setChecked(False)
        self.checkBox_gen_SG.setChecked(False)
        self.checkBox_gen_ST.setChecked(False)
        self.checkBox_gen_RL.setChecked(False)
        self.checkBox_gen_NP.setChecked(False)
        self.checkBox_gen_LB.setChecked(False)
        self.checkBox_gen_LO.setChecked(False)
        self.checkBox_gen_HF.setChecked(False)
        
        self.checkBox_int_FN.setChecked(False)
        self.checkBox_int_WD.setChecked(False)
        self.checkBox_int_BU.setChecked(False)
        self.checkBox_int_BM.setChecked(False)
        self.checkBox_int_EM.setChecked(False)
        self.checkBox_int_TS.setChecked(False)
        self.checkBox_int_SY.setChecked(False)
        self.checkBox_int_FA.setChecked(False)
        self.checkBox_int_GA.setChecked(False)
        self.checkBox_int_WR.setChecked(False)
        self.checkBox_int_DR.setChecked(False)
        self.checkBox_int_DG.setChecked(False)
        self.checkBox_int_SC.setChecked(False)
        self.checkBox_int_PB.setChecked(False)
        self.checkBox_int_SR.setChecked(False)
        self.checkBox_int_RP.setChecked(False)
        self.checkBox_int_CO.setChecked(False)
        self.checkBox_int_OG.setChecked(False)
        self.checkBox_int_SL.setChecked(False)
        
        self.checkBox_fet_RA.setChecked(False)
        self.checkBox_fet_CR.setChecked(False)
        self.checkBox_fet_LD.setChecked(False)
        self.checkBox_fet_RC.setChecked(False)
        self.checkBox_fet_TO.setChecked(False)
        self.checkBox_fet_TR.setChecked(False)
        self.checkBox_fet_GR.setChecked(False)
        self.checkBox_fet_FC.setChecked(False)
        self.checkBox_fet_HE.setChecked(False)
        self.checkBox_fet_IS.setChecked(False)
        self.checkBox_fet_AB.setChecked(False)
        self.checkBox_fet_PN.setChecked(False)
        self.checkBox_fet_CH.setChecked(False)
        self.checkBox_fet_BD.setChecked(False)
        self.checkBox_fet_FE.setChecked(False)
        self.checkBox_fet_OR.setChecked(False)
        
        self.checkBox_gro_SP.setChecked(False)
        self.checkBox_gro_PE.setChecked(False)
        self.checkBox_gro_PO.setChecked(False)
        self.checkBox_gro_VO.setChecked(False)
        
        self.checkBox_inc_MO.setChecked(False)
        self.checkBox_inc_FD.setChecked(False)
        self.checkBox_inc_BS.setChecked(False)
        self.checkBox_inc_MD.setChecked(False)
        self.checkBox_inc_FI.setChecked(False)
        self.checkBox_inc_EF.setChecked(False)
        self.checkBox_inc_JF.setChecked(False)
        self.checkBox_inc_RI.setChecked(False)
        self.checkBox_inc_GI.setChecked(False)
        self.checkBox_inc_MU.setChecked(False)
        self.checkBox_inc_FR.setChecked(False)
        self.checkBox_inc_PR.setChecked(False)
        self.checkBox_inc_BL.setChecked(False)
        
        self.checkBox_voy_VR.setChecked(False)
        self.checkBox_voy_VP.setChecked(False)
        self.checkBox_voy_VF.setChecked(False)
        self.checkBox_voy_MB.setChecked(False)
        self.checkBox_voy_WC.setChecked(False)
        
        self.checkBox_idl_U14.setChecked(False)
        self.checkBox_idl_O14.setChecked(False)
        self.checkBox_idl_AD.setChecked(False)
        
        self.checkBox_oth_FO.setChecked(False)
        self.checkBox_oth_QV.setChecked(False)
        self.checkBox_oth_BQ.setChecked(False)
        self.checkBox_oth_UC.setChecked(False)
        self.checkBox_oth_CL.setChecked(False)
        
        self.checkBox_girl_GN.setChecked(False)
        self.checkBox_girl_TN.setChecked(False)
        self.checkBox_girl_FT.setChecked(False)
        self.checkBox_girl_MS.setChecked(False)
        self.checkBox_girl_SK.setChecked(False)
        self.checkBox_girl_CB.setChecked(False)
        self.checkBox_girl_DA.setChecked(False)
        self.checkBox_girl_TI.setChecked(False)
        self.checkBox_girl_TL.setChecked(False)
        self.checkBox_girl_BG.setChecked(False)
        self.checkBox_girl_SH.setChecked(False)
        self.checkBox_girl_TB.setChecked(False)
        self.checkBox_girl_CU.setChecked(False)
        self.checkBox_girl_VI.setChecked(False)
        self.checkBox_girl_AV.setChecked(False)
        self.checkBox_girl_CS.setChecked(False)
        self.checkBox_girl_GF.setChecked(False)
        self.checkBox_girl_FB.setChecked(False)
        
        self.checkBox_series_MUS.setChecked(False)
        self.checkBox_series_BAK.setChecked(False)
        self.checkBox_series_N24.setChecked(False)
        self.checkBox_series_RRA.setChecked(False)
        self.checkBox_series_CND.setChecked(False)
        self.checkBox_series_GQU.setChecked(False)
        self.checkBox_series_RTG.setChecked(False)
        self.checkBox_series_SPK.setChecked(False)
    
    def buildResPath(self, relative):
        directory = path.dirname(sys.argv[0])
        return path.join(directory, relative)
    
    