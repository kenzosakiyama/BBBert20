#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Criacao: Jan 2020a
Atualizado: '--'--
@author: calusbr@gmail.com
Title: Run Crawler Twitter BBB20
Api: Twint https://github.com/twintproject/twint
'''
####################################################################################################
# LIBS
####################################################################################################
import twint
import time
####################################################################################################
# 1 ELIMINAÇÃO - 2 PARTICIPANTES (Lucas Chumbo vs Bia Andrade)
####################################################################################################
for x in range(4):
    '''
    c = twint.Config()
    c.Search = "@lucaschumbo"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/1-eliminacao/lucas_chumbo_"+str(x)+"_1p.csv"
    c.Since = "2020-01-26 22:00:00"
    c.Until = "2020-01-28 20:00:00"
    c.Count = True
    c.Skip_certs = True
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "chumbo bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/1-eliminacao/lucas_chumbo_"+str(x)+"_1p.csv"
    c.Since = "2020-01-26 22:00:00"
    c.Until = "2020-01-28 20:00:00"
    c.Count = True
    c.Skip_certs = True
    twint.run.Search(c)
    ####################################################################################################

    c = twint.Config()
    c.Search = "@BiaAndradeOfc"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/1-eliminacao/bia_andrade_"+str(x)+"_1p.csv"
    c.Since = "2020-01-26 22:00:00"
    c.Until = "2020-01-28 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "bianca andrade bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/1-eliminacao/bia_andrade_"+str(x)+"_1p.csv"
    c.Since = "2020-01-26 22:00:00"
    c.Until = "2020-01-28 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "boca rosa bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/1-eliminacao/bia_andrade_"+str(x)+"_1p.csv"
    c.Since = "2020-01-26 22:00:00"
    c.Until = "2020-01-28 20:00:00"
    twint.run.Search(c)
    ####################################################################################################
    # 2 ELIMINAÇÃO - 4 PARTICIPANTES (Babu vs Petrix vs Pyong vs Hadson)
    ####################################################################################################

    c = twint.Config()
    c.Search = "@BabuSantana"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/2-eliminacao/babu_santana_"+str(x)+"_2p.csv"
    c.Since = "2020-02-02 22:00:00"
    c.Until = "2020-02-04 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Babu bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/2-eliminacao/babu_santana_"+str(x)+"_2p.csv"
    c.Since = "2020-02-02 22:00:00"
    c.Until = "2020-02-04 20:00:00"
    twint.run.Search(c)
    ####################################################################################################
    
    c = twint.Config()
    c.Search = "@petrixbarbosa"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/2-eliminacao/petrix_"+str(x)+"_2p.csv"
    c.Since = "2020-02-02 22:00:00"
    c.Until = "2020-02-04 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "petrix bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/2-eliminacao/petrix_"+str(x)+"_2p.csv"
    c.Since = "2020-02-02 22:00:00"
    c.Until = "2020-02-04 20:00:00"
    twint.run.Search(c)
    ####################################################################################################

    c = twint.Config()
    c.Search = "@PyongLeeTV"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/2-eliminacao/pyong_"+str(x)+"_2p.csv"
    c.Since = "2020-02-02 22:00:00"
    c.Until = "2020-02-04 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Pyong bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/2-eliminacao/pyong_"+str(x)+"_2p.csv"
    c.Since = "2020-02-02 22:00:00"
    c.Until = "2020-02-04 20:00:00"
    twint.run.Search(c)
    ####################################################################################################

    c = twint.Config()
    c.Search = "@HadsonNery"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/2-eliminacao/hadson_"+str(x)+"_2p.csv"
    c.Since = "2020-02-02 22:00:00"
    c.Until = "2020-02-04 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Hadson bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/2-eliminacao/hadson_"+str(x)+"_2p.csv"
    c.Since = "2020-02-02 22:00:00"
    c.Until = "2020-02-04 20:00:00"
    twint.run.Search(c)
    ####################################################################################################
    # 3 ELIMINAÇÃO - 2 PARTICIPANTES (Felipe vs Hadson)
    ####################################################################################################

    c = twint.Config()
    c.Search = "@HadsonNery"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/3-eliminacao/hadson_"+str(x)+"_3p.csv"
    c.Since = "2020-02-09 22:00:00"
    c.Until = "2020-02-11 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Hadson bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/3-eliminacao/hadson_"+str(x)+"_3p.csv"
    c.Since = "2020-02-09 22:00:00"
    c.Until = "2020-02-11 20:00:00"
    twint.run.Search(c)
    ####################################################################################################

    c = twint.Config()
    c.Search = "@felipeprior"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/3-eliminacao/felipe_prior_"+str(x)+"_3p.csv"
    c.Since = "2020-02-09 22:00:00"
    c.Until = "2020-02-11 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "prior bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/3-eliminacao/felipe_prior_"+str(x)+"_3p.csv"
    c.Since = "2020-02-09 22:00:00"
    c.Until = "2020-02-11 20:00:00"
    twint.run.Search(c)
    ####################################################################################################
    # 4 ELIMINAÇÃO - 3 PARTICIPANTES (Babu vs Lucas vs Victor Hugo)
    ####################################################################################################

    c = twint.Config()
    c.Search = "@BabuSantana"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/4-eliminacao/babu_santana_"+str(x)+"_4p.csv"
    c.Since = "2020-02-16 22:00:00"
    c.Until = "2020-02-18 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Babu bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/4-eliminacao/babu_santana_"+str(x)+"_4p.csv"
    c.Since = "2020-02-16 22:00:00"
    c.Until = "2020-02-18 20:00:00"
    twint.run.Search(c)
    ####################################################################################################

    c = twint.Config()
    c.Search = "@LucasBGallina"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/4-eliminacao/lucas_"+str(x)+"_4p.csv"
    c.Since = "2020-02-16 22:00:00"
    c.Until = "2020-02-18 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Lucas bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/4-eliminacao/lucas_"+str(x)+"_4p.csv"
    c.Since = "2020-02-16 22:00:00"
    c.Until = "2020-02-18 20:00:00"
    twint.run.Search(c)
    ####################################################################################################

    c = twint.Config()
    c.Search = "@victorhugotex"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/4-eliminacao/victorhugotex_"+str(x)+"_4p.csv"
    c.Since = "2020-02-16 22:00:00"
    c.Until = "2020-02-18 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "victor bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/4-eliminacao/victorhugotex_"+str(x)+"_4p.csv"
    c.Since = "2020-02-16 22:00:00"
    c.Until = "2020-02-18 20:00:00"
    twint.run.Search(c)
    ####################################################################################################
    # 5 ELIMINAÇÃO - 3 PARTICIPANTES (Bianca vs Felipe vs Flay)
    ####################################################################################################

    c = twint.Config()
    c.Search = "@BiaAndradeOfc"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/5-eliminacao/bia_andrade_"+str(x)+"_5p.csv"
    c.Since = "2020-02-23 22:00:00"
    c.Until = "2020-02-25 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "bianca andrade bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/1-eliminacao/bia_andrade_"+str(x)+"_1p.csv"
    c.Since = "2020-02-23 22:00:00"
    c.Until = "2020-02-25 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "boca rosa bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/1-eliminacao/bia_andrade_"+str(x)+"_1p.csv"
    c.Since = "2020-02-23 22:00:00"
    c.Until = "2020-02-25 20:00:00"
    twint.run.Search(c)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@felipeprior"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/5-eliminacao/felipe_prior_"+str(x)+"_5p.csv"
    c.Since = "2020-02-23 22:00:00"
    c.Until = "2020-02-25 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "prior bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/5-eliminacao/felipe_prior_"+str(x)+"_5p.csv"
    c.Since = "2020-02-23 22:00:00"
    c.Until = "2020-02-25 20:00:00"
    twint.run.Search(c)

    ####################################################################################################
    c = twint.Config()
    c.Search = "@laneeoficial"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/5-eliminacao/flay_"+str(x)+"_5p.csv"
    c.Since = "2020-02-23 22:00:00"
    c.Until = "2020-02-25 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Flay bbb20`"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/5-eliminacao/flay_"+str(x)+"_5p.csv"
    c.Since = "2020-02-23 22:00:00"
    c.Until = "2020-02-25 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    # 6 ELIMINAÇÃO - 3 PARTICIPANTES (Guilherme vs Pyong vs Gizelly)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@PyongLeeTV"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/6-eliminacao/pyong_"+str(x)+"_6p.csv"
    c.Since = "2020-03-01 22:00:00"
    c.Until = "2020-03-03 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Pyong bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/6-eliminacao/pyong_"+str(x)+"_6p.csv"
    c.Since = "2020-03-01 22:00:00"
    c.Until = "2020-03-03 20:00:00"
    twint.run.Search(c)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@gizellybicalho_"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/6-eliminacao/gizellybicalho_"+str(x)+"_6p.csv"
    c.Since = "2020-03-01 22:00:00"
    c.Until = "2020-03-03 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Gizelly bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/6-eliminacao/gizellybicalho_"+str(x)+"_6p.csv"
    c.Since = "2020-03-01 22:00:00"
    c.Until = "2020-03-03 20:00:00"
    twint.run.Search(c)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@guinapolitano"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/6-eliminacao/guinapolitano_"+str(x)+"_6p.csv"
    c.Since = "2020-03-01 22:00:00"
    c.Until = "2020-03-03 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Guilherme bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/6-eliminacao/guinapolitano_"+str(x)+"_6p.csv"
    c.Since = "2020-03-01 22:00:00"
    c.Until = "2020-03-03 20:00:00"
    twint.run.Search(c)

    ####################################################################################################
    # 7 ELIMINAÇÃO - 3 PARTICIPANTES (Manu vs Victor Hugo vs Babu)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@manugavassi"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/7-eliminacao/manugavassi_"+str(x)+"_7p.csv"
    c.Since = "2020-03-08 22:00:00"
    c.Until = "2020-03-10 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Manu bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/7-eliminacao/manugavassi_"+str(x)+"_7p.csv"
    c.Since = "2020-03-08 22:00:00"
    c.Until = "2020-03-10 20:00:00"
    twint.run.Search(c)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@BabuSantana"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/7-eliminacao/BabuSantana_"+str(x)+"_7p.csv"
    c.Since = "2020-03-08 22:00:00"
    c.Until = "2020-03-10 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Babu bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/7-eliminacao/BabuSantana_"+str(x)+"_7p.csv"
    c.Since = "2020-03-08 22:00:00"
    c.Until = "2020-03-10 20:00:00"
    twint.run.Search(c)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@victorhugotex"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/7-eliminacao/victorhugotex_"+str(x)+"_7p.csv"
    c.Since = "2020-03-08 22:00:00"
    c.Until = "2020-03-10 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Victor bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/7-eliminacao/victorhugotex_"+str(x)+"_7p.csv"
    c.Since = "2020-03-08 22:00:00"
    c.Until = "2020-03-10 20:00:00"
    twint.run.Search(c)

    ####################################################################################################
    # 8 ELIMINAÇÃO - 3 PARTICIPANTES (Babu vs Rafa vs Pyong)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@BabuSantana"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/8-eliminacao/BabuSantana_"+str(x)+"_8p.csv"
    c.Since = "2020-03-15 22:00:00"
    c.Until = "2020-03-17 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Babu bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/8-eliminacao/BabuSantana_"+str(x)+"_8p.csv"
    c.Since = "2020-03-15 22:00:00"
    c.Until = "2020-03-17 20:00:00"
    twint.run.Search(c)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@PyongLeeTV"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/8-eliminacao/pyong_"+str(x)+"_8p.csv"
    c.Since = "2020-03-15 22:00:00"
    c.Until = "2020-03-17 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Pyong bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/8-eliminacao/pyong_"+str(x)+"_8p.csv"
    c.Since = "2020-03-15 22:00:00"
    c.Until = "2020-03-17 20:00:00"
    twint.run.Search(c)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@rafakalimann_"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/8-eliminacao/rafa_"+str(x)+"_8p.csv"
    c.Since = "2020-03-15 22:00:00"
    c.Until = "2020-03-17 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Rafa bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/8-eliminacao/rafa_"+str(x)+"_8p.csv"
    c.Since = "2020-03-15 22:00:00"
    c.Until = "2020-03-17 20:00:00"
    twint.run.Search(c)

    ####################################################################################################
    # 9 ELIMINAÇÃO - 3 PARTICIPANTES (Flay vs Daniel vs Ivy)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@laneeoficial"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/9-eliminacao/Flay_"+str(x)+"_9p.csv"
    c.Since = "2020-03-22 22:00:00"
    c.Until = "2020-03-24 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Flay bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/9-eliminacao/Flay_"+str(x)+"_9p.csv"
    c.Since = "2020-03-22 22:00:00"
    c.Until = "2020-03-24 20:00:00"
    twint.run.Search(c)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@DanielLenhardt_"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/9-eliminacao/Daniel_"+str(x)+"_9p.csv"
    c.Since = "2020-03-22 22:00:00"
    c.Until = "2020-03-24 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Daniel bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/9-eliminacao/Daniel_"+str(x)+"_9p.csv"
    c.Since = "2020-03-22 22:00:00"
    c.Until = "2020-03-24 20:00:00"
    twint.run.Search(c)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@IvyMoraesss"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/9-eliminacao/Ivy_"+str(x)+"_9p.csv"
    c.Since = "2020-03-22 22:00:00"
    c.Until = "2020-03-24 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Ivy bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/9-eliminacao/Ivy_"+str(x)+"_9p.csv"
    c.Since = "2020-03-22 22:00:00"
    c.Until = "2020-03-24 20:00:00"
    twint.run.Search(c)

    ####################################################################################################
    # 10 ELIMINAÇÃO - 3 PARTICIPANTES (Prior vs Mari vs Manu)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@felipeprior"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/10-eliminacao/prior_"+str(x)+"_10p.csv"
    c.Since = "2020-03-29 22:00:00"
    c.Until = "2020-03-31 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Prior bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/10-eliminacao/prior_"+str(x)+"_10p.csv"
    c.Since = "2020-03-29 22:00:00"
    c.Until = "2020-03-31 20:00:00"
    twint.run.Search(c)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@manugavassi"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/10-eliminacao/manu_"+str(x)+"_10p.csv"
    c.Since = "2020-03-29 22:00:00"
    c.Until = "2020-03-31 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Manu bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/10-eliminacao/manu_"+str(x)+"_10p.csv"
    c.Since = "2020-03-29 22:00:00"
    c.Until = "2020-03-31 20:00:00"
    twint.run.Search(c)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@marigonzalez"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/10-eliminacao/mari_"+str(x)+"_10p.csv"
    c.Since = "2020-03-29 22:00:00"
    c.Until = "2020-03-31 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Mari bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/10-eliminacao/mari_"+str(x)+"_10p.csv"
    c.Since = "2020-03-29 22:00:00"
    c.Until = "2020-03-31 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    # 11 ELIMINAÇÃO - 3 PARTICIPANTES ()
    ####################################################################################################
    c = twint.Config()
    c.Search = "@BabuSantana"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/11-eliminacao/babu_"+str(x)+"_11p.csv"
    c.Since = "2020-04-03 22:00:00"
    c.Until = "2020-04-05 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Babu bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/11-eliminacao/babu_"+str(x)+"_11p.csv"
    c.Since = "2020-04-03 22:00:00"
    c.Until = "2020-04-05 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    c = twint.Config()
    c.Search = "@GabiMartinsOF"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/11-eliminacao/gabi_"+str(x)+"_11p.csv"
    c.Since = "2020-04-03 22:00:00"
    c.Until = "2020-04-05 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Gabi bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/11-eliminacao/gabi_"+str(x)+"_11p.csv"
    c.Since = "2020-04-03 22:00:00"
    c.Until = "2020-04-05 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    c = twint.Config()
    c.Search = "@thelminha_assis"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/11-eliminacao/thelma_"+str(x)+"_11p.csv"
    c.Since = "2020-04-03 22:00:00"
    c.Until = "2020-04-05 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Thelma bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/11-eliminacao/thelma_"+str(x)+"_11p.csv"
    c.Since = "2020-04-03 22:00:00"
    c.Until = "2020-04-05 20:00:00"
    twint.run.Search(c)

    ####################################################################################################
    # 12 ELIMINAÇÃO - 3 PARTICIPANTES (Babu, Flay, Marcela)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@BabuSantana"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/12-eliminacao/babu_"+str(x)+"_12p.csv"
    c.Since = "2020-04-05 22:00:00"
    c.Until = "2020-04-07 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Babu bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/12-eliminacao/babu_"+str(x)+"_12p.csv"
    c.Since = "2020-04-05 22:00:00"
    c.Until = "2020-04-07 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    c = twint.Config()
    c.Search = "@laneeoficial"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/12-eliminacao/flay_"+str(x)+"_12p.csv"
    c.Since = "2020-04-05 22:00:00"
    c.Until = "2020-04-07 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Flay bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/12-eliminacao/flay_"+str(x)+"_12p.csv"
    c.Since = "2020-04-05 22:00:00"
    c.Until = "2020-04-07 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    c = twint.Config()
    c.Search = "@marcelamcgowan"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/12-eliminacao/marcela_"+str(x)+"_12p.csv"
    c.Since = "2020-04-05 22:00:00"
    c.Until = "2020-04-07 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Marcela bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/12-eliminacao/marcela_"+str(x)+"_12p.csv"
    c.Since = "2020-04-05 22:00:00"
    c.Until = "2020-04-07 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    # 13 ELIMINAÇÃO - 3 PARTICIPANTES (Babu, Flay, Thelma)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@BabuSantana"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/13-eliminacao/babu_"+str(x)+"_13p.csv"
    c.Since = "2020-04-10 22:00:00"
    c.Until = "2020-04-12 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Babu bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/13-eliminacao/babu_"+str(x)+"_13p.csv"
    c.Since = "2020-04-10 22:00:00"
    c.Until = "2020-04-12 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    c = twint.Config()
    c.Search = "@laneeoficial"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/13-eliminacao/flay_"+str(x)+"_13p.csv"
    c.Since = "2020-04-10 22:00:00"
    c.Until = "2020-04-12 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Flay bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/13-eliminacao/flay_"+str(x)+"_13p.csv"
    c.Since = "2020-04-10 22:00:00"
    c.Until = "2020-04-12 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    c = twint.Config()
    c.Search = "@thelminha_assis"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/13-eliminacao/thelma_"+str(x)+"_13p.csv"
    c.Since = "2020-04-10 22:00:00"
    c.Until = "2020-04-12 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Thelma bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/13-eliminacao/thelma_"+str(x)+"_13p.csv"
    c.Since = "2020-04-10 22:00:00"
    c.Until = "2020-04-12 20:00:00"
    twint.run.Search(c)

    ####################################################################################################
    # 14 ELIMINAÇÃO - 3 PARTICIPANTES (Babu, Mari , Gizelly)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@BabuSantana"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/14-eliminacao/babu_"+str(x)+"_14p.csv"
    c.Since = "2020-04-12 22:00:00"
    c.Until = "2020-04-14 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Babu bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/14-eliminacao/babu_"+str(x)+"_14p.csv"
    c.Since = "2020-04-12 22:00:00"
    c.Until = "2020-04-14 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    c = twint.Config()
    c.Search = "@marigonzalez"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/14-eliminacao/mari_"+str(x)+"_14p.csv"
    c.Since = "2020-04-12 22:00:00"
    c.Until = "2020-04-14 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Mari bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/14-eliminacao/mari_"+str(x)+"_14p.csv"
    c.Since = "2020-04-12 22:00:00"
    c.Until = "2020-04-14 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    c = twint.Config()
    c.Search = "@gizellybicalho_"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/14-eliminacao/gizelly_"+str(x)+"_14p.csv"
    c.Since = "2020-04-12 22:00:00"
    c.Until = "2020-04-14 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Gizelly bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/14-eliminacao/gizelly_"+str(x)+"_14p.csv"
    c.Since = "2020-04-12 22:00:00"
    c.Until = "2020-04-14 20:00:00"
    twint.run.Search(c)
    ####################################################################################################
    # 15 ELIMINAÇÃO - 3 PARTICIPANTES (Ivy, Thelma, Rafa)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@IvyMoraesss"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/15-eliminacao/ivy_"+str(x)+"_15p.csv"
    c.Since = "2020-04-17 22:00:00"
    c.Until = "2020-04-19 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Ivy bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/15-eliminacao/ivy_"+str(x)+"_15p.csv"
    c.Since = "2020-04-17 22:00:00"
    c.Until = "2020-04-19 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    c = twint.Config()
    c.Search = "@thelminha_assis"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/15-eliminacao/thelma_"+str(x)+"_15p.csv"
    c.Since = "2020-04-17 22:00:00"
    c.Until = "2020-04-19 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Thelma bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/15-eliminacao/thelma_"+str(x)+"_15p.csv"
    c.Since = "2020-04-17 22:00:00"
    c.Until = "2020-04-19 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    c = twint.Config()
    c.Search = "@rafakalimann_"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/15-eliminacao/rafa_"+str(x)+"_15p.csv"
    c.Since = "2020-04-17 22:00:00"
    c.Until = "2020-04-19 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Rafa bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/15-eliminacao/rafa_"+str(x)+"_15p.csv"
    c.Since = "2020-04-17 22:00:00"
    c.Until = "2020-04-19 20:00:00"
    twint.run.Search(c)
    ####################################################################################################
    # 16 ELIMINAÇÃO - 3 PARTICIPANTES (Babu, Mari, Manu)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@BabuSantana"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/16-eliminacao/babu_"+str(x)+"_16p.csv"
    c.Since = "2020-04-19 22:00:00"
    c.Until = "2020-04-21 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Babu bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/16-eliminacao/babu_"+str(x)+"_16p.csv"
    c.Since = "2020-04-19 22:00:00"
    c.Until = "2020-04-21 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    c = twint.Config()
    c.Search = "@manugavassi"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/16-eliminacao/manu_"+str(x)+"_16p.csv"
    c.Since = "2020-04-19 22:00:00"
    c.Until = "2020-04-21 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Manu bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/16-eliminacao/manu_"+str(x)+"_16p.csv"
    c.Since = "2020-04-19 22:00:00"
    c.Until = "2020-04-21 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    c = twint.Config()
    c.Search = "@marigonzalez"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/16-eliminacao/mari_"+str(x)+"_16p.csv"
    c.Since = "2020-04-19 22:00:00"
    c.Until = "2020-04-21 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Mari bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/16-eliminacao/mari_"+str(x)+"_16p.csv"
    c.Since = "2020-04-19 22:00:00"
    c.Until = "2020-04-21 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    # 17 ELIMINAÇÃO - 3 PARTICIPANTES (Babu, Rafa, Thelma)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@BabuSantana"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/17-eliminacao/babu_"+str(x)+"_17p.csv"
    c.Since = "2020-04-23 22:00:00"
    c.Until = "2020-04-25 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Babu bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/17-eliminacao/babu_"+str(x)+"_17p.csv"
    c.Since = "2020-04-23 22:00:00"
    c.Until = "2020-04-25 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    c = twint.Config()
    c.Search = "@thelminha_assis"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/17-eliminacao/thelma_"+str(x)+"_17p.csv"
    c.Since = "2020-04-23 22:00:00"
    c.Until = "2020-04-25 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Thelma bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/17-eliminacao/thelma_"+str(x)+"_17p.csv"
    c.Since = "2020-04-23 22:00:00"
    c.Until = "2020-04-25 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    c = twint.Config()
    c.Search = "@rafakalimann_"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/17-eliminacao/rafa_"+str(x)+"_17p.csv"
    c.Since = "2020-04-23 22:00:00"
    c.Until = "2020-04-25 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Rafa bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/17-eliminacao/rafa_"+str(x)+"_17p.csv"
    c.Since = "2020-04-23 22:00:00"
    c.Until = "2020-04-25 20:00:00"
    twint.run.Search(c)
    '''
    ####################################################################################################
    # FINAL - 3 PARTICIPANTES (Manu, Rafa, Thelma)
    ####################################################################################################
    c = twint.Config()
    c.Search = "@manugavassi"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/18-eliminacao/manu_"+str(x)+"_18p.csv"
    c.Since = "2020-04-23 22:00:00"
    c.Until = "2020-04-25 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Manu bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/18-eliminacao/manu_"+str(x)+"_18p.csv"
    c.Since = "2020-04-23 22:00:00"
    c.Until = "2020-04-25 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    c = twint.Config()
    c.Search = "@thelminha_assis"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/18-eliminacao/thelma_"+str(x)+"_18p.csv"
    c.Since = "2020-04-23 22:00:00"
    c.Until = "2020-04-25 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Thelma bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/18-eliminacao/thelma_"+str(x)+"_18p.csv"
    c.Since = "2020-04-23 22:00:00"
    c.Until = "2020-04-25 20:00:00"
    twint.run.Search(c)
    
    ####################################################################################################
    c = twint.Config()
    c.Search = "@rafakalimann_"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/18-eliminacao/rafa_"+str(x)+"_18p.csv"
    c.Since = "2020-04-23 22:00:00"
    c.Until = "2020-04-25 20:00:00"
    twint.run.Search(c)

    c = twint.Config()
    c.Search = "Rafa bbb20"
    c.Store_csv = True
    c.Output = "/home/lucasr/datasets/tweets/bbb20/18-eliminacao/rafa_"+str(x)+"_18p.csv"
    c.Since = "2020-04-23 22:00:00"
    c.Until = "2020-04-25 20:00:00"
    twint.run.Search(c)