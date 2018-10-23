#!/usr/bin/python
# -*- coding: latin-1 -*-
'''
Definire una funzione es3(lista, testo) che prende:
- una lista di parole (nessuna delle quali e' prefisso dell'altra)
- una stringa di testo. Il testo e' stato ottenuto concatenando alcune delle parole presenti nella lista 'lista'
  (una stessa parola puo' comparire piu' volte nella stringa di testo).
- restituisce una coppia (tupla) formata da:
        - la lista delle parole che, concatenate producono il testo
        - la parola che vi occorre piu' spesso
  (se questa parola non e' unica allora viene restituita quella che precede le altre lessicograficamente).
  Nella lista di output ogni parola appare una sola volta e le parole
  risultano ordinate in base alla loro prima apparizione nella concatenazione che produce il testo
  (i.e. quella che compare per prima al primo posto ecc.ecc.)
  Infine al termine della funzione la lista 'lista' deve risultare modificata come segue:
  in essa saranno state cancellate tutte le parole utilizzate in testo, e tornate come risultato.
  Ad esempio: se lista=['gatto','cane','topo']
  - con  testo='topogattotopotopogattogatto' la risposta e' la coppia (['topo','gatto'],'gatto')
    e lista diviene ['cane']
  se lista=['ala','cena','elica','nave','luce','lana','vela']
  - con testo='lucenavelanavelanaveelica' la risposta e' (['luce','nave','lana','vela','elica'],'nave')
  e ls diviene ['ala','cena']

NOTA: il timeout previsto per questo esercizio è di 5 secondi per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 (ad esempio editatelo dentro Spyder)
'''
import time

def es3(lista, testo):
  resulting_words = []
  most_common_word = ""

  return (resulting_words, most_common_word)

print(es3(["gatto", "cane", "topo"], "topogattotopotopogattogatto"))

def test():
  res = es3(["AgPU", "Ahur", "BaPP", "DAFo", "DNiO", "ENBR", "EzEe", "FQZg", "FRsi", "GdLC",
      "Gptg", "HLZD", "HMQq", "ITbq", "ItQT", "Itgc", "LqFA", "MLhb", "MLlg", "MbZF", "NESc", 
      "NFMB", "Novu", "PqVO", "QBPM", "QCfH", "QSnf", "QcSp", "QsLz", "QsPH", "Resh", "RzVG", 
      "Sgzb", "SoMg", "TNsC", "TaHt", "UEub", "UnBu", "Vqrz", "VuhA", "ZmmN", "Zqde", "aEAm", 
      "aUaf", "anOz", "aoPQ", "atrt", "auTz", "bLcv", "bVau", "bZPa", "bqbE", "cFeD", "cefb", 
      "cmHN", "dBSi", "eNnn", "eRQq", "ecfi", "eevv", "etQe", "fHfZ", "gMbD", "gsNp", "hcor", 
      "iAhU", "iSQg", "iplP", "istE", "lzvg", "mNpv", "mOEC", "mPpt", "mUNc", "mgGD", "mhHm", 
      "mmsO", "nUfq", "nzSv", "oBgp", "orCf", "ozRi", "pGbO", "pUPL", "pZzc", "qDvc", "qOZb", 
      "qqIu", "rEFn", "rqbr", "rseH", "snPp", "tCuR", "tZuI", "uNMb", "vGPm", "vQCm", "vipd", 
      "zTIh", "zUQp"], "NovuMbZFSgzbcmHNQcSpmPpttCuRvQCmEzEegsNpqqIubZPasnPpozRianOzbVauNFMBlzvgtZuIENBRiplPHLZDSgzborCfHMQqTNsCMLhbzUQpnzSvpZzcqqIueNnnReshdBSibZPaNFMBZqdeeNnnLqFAoBgpgMbDQcSpdBSiistEcFeDpZzcUnBuTaHtRzVGvGPmmOECAgPUQBPMiplPeNnnmgGDBaPPDAFoorCfRzVGSoMgQSnfNovuUEubMLlglzvgQCfHTNsCVuhAmgGDvQCmSgzbqqIueRQqNFMBlzvgaoPQgMbDcefbzTIhQSnfbVauQSnfUEubITbqDAFomPptvGPmAhurlzvgUnBuqOZbvipdtCuRpUPLMLhbGdLChcorauTzVuhAdBSihcorqOZbaoPQvipdiplPZqdeAgPUeNnnsnPpeRQqanOzVuhAlzvgbqbEaUaftZuIqqIugsNpItQTpGbOQSnfmOECAgPUTaHtozRitCuRtZuIQCfHiSQgcFeDvGPmsnPpVuhANFMBeRQqoBgpqDvciplPQCfHatrtiplPAgPUqOZbbVaumgGDcmHNbqbEaUafoBgpmgGDtZuIvGPmFRsigsNpvGPmRzVGozRipUPLUnBuorCfBaPPcFeDtCuRorCfMbZFozRizUQpbZPaTNsCNovuzTIhGdLCzUQpAhuranOzSoMgrseHcFeDqqIulzvgVqrzMbZFSoMggMbDNFMBENBRTNsCHMQqvGPmmhHmcmHNFRsiaoPQFRsipZzceNnnBaPPNFMBhcorrseHNEScrEFnHLZDbqbEozRirEFnTaHtVqrzQSnfiplPQSnfReshaEAmTNsCFRsiGdLCiSQgpZzcauTzmOECEzEeNFMBVqrzpUPLsnPpmOECTNsCaoPQnzSvQsPHbZPamOECbqbENovufHfZSoMgnzSvaEAmsnPpQsLzSoMgnzSvrseHRzVGpZzcDAFooBgpbqbEZmmNdBSivipdRzVGTNsCQBPMGdLCorCftZuINFMBmgGDeNnnmgGDtZuIMLlgSoMgecfiiplPNEScMLhbzUQpMLhbsnPpeNnnatrtVuhAvQCmbqbEReshItQTsnPpQSnfsnPpqqIuVuhAFRsiITbqQsPHbZPaZqdegsNpHMQqPqVOENBRFQZgBaPPvQCmQcSpqqIuDNiOgsNprseHiplPtCuRnzSveNnnaUafpZzcTaHtnzSvrEFnNovuHMQqQsLzbqbEQsPHgsNpeRQqvQCmNFMBQsPHReshUEubmNpvmgGDbVauQcSpeRQqsnPpSoMgaEAmgsNpmhHmItQTQcSpENBRAhurAgPUfHfZZmmNbVaumgGDUEubQCfHbqbENEScvipdpGbOMbZFDAFoAhurbVauMLlgqDvclzvgFQZgmPptSgzbLqFApUPLVqrzAhurDNiOistEFQZgiplPLqFAENBRTaHtzUQpdBSiHLZDQBPMDAFogsNpozRiLqFAvGPmTaHtqqIuQBPMpZzceRQqbVauaEAmorCfTNsCSoMgpGbOozRiRzVGRzVGFQZgmhHmmhHmNovuanOzcmHNmOECozRiiSQgFQZgaoPQmNpvcFeDistEQCfHsnPpistEcmHNpZzcFRsisnPpTNsCvGPmnzSvtCuRvQCmGdLCSgzbNovuHMQqMbZFFQZgQSnfcmHNENBREzEeozRiHLZDetQehcorauTzHMQqZmmNENBRLqFAistEDNiOeNnnqDvcLqFAbZPavipdrseHeRQqDAFoiplPTNsCHLZDSgzbZqdeVqrzDNiObVauFQZgtZuISoMgZmmNLqFASoMgItQTqOZbVqrzHMQqcmHNRzVGhcormOECQSnfaEAmaUafbZPamgGDfHfZITbqLqFApUPLeRQqiplPmOECtCuRmgGDiSQgistEDAFoUnBuvGPmNEScQCfHauTzbVauiSQgZqdeHMQqcFeDanOzLqFAFRsiENBRVqrzpUPListEZmmNcefbVqrzZmmNaoPQTNsCZqdevGPmvGPmiSQghcorAhuriplPMbZFZmmNtZuIZqdeZqdeFRsieRQqTaHtfHfZecfiatrtmgGDFQZgMLhbEzEeiplPgMbDSgzbRzVGvGPmaUafatrtpGbOauTzbqbEVuhAaUafistEhcorNFMBDAFoMLlgSgzbqqIuQsLzmPptMLhbItQTPqVOzTIhcFeDtZuIoBgpEzEeHMQqlzvgqqIuTNsCsnPpITbqQSnfSoMgFRsiorCfiplPpGbOGdLCQcSppGbONovudBSiBaPPmhHmauTzgMbDrseHUEubQsLzQCfHgsNpReshcmHNeRQqqOZbatrtlzvgQBPMfHfZtCuRGdLCSgzbcFeDQCfHAhurvGPmistEzTIhgMbDGdLCbqbEnzSvmgGDmgGDcmHNENBRaoPQecfiAgPUQBPMVqrzrEFnpGbOAgPUlzvgVqrzvGPmZmmNzUQplzvgpGbOmNpvUEubiplPcFeDlzvgiSQgcFeDorCfmgGDVuhAeRQqVqrzLqFAhcoreNnnmhHmMLhbmNpvzTIhNEScSgzbozRiAhurcmHNpZzcmPptDNiOauTzcefbbqbEUEubpZzcvQCmqDvcBaPPHLZDHLZDAgPUbVauTNsCTNsCauTzozRivGPmfHfZzTIhaUafbVauecfiItQTfHfZaoPQMLlgcefbMLlgBaPPNovuSoMgauTzLqFAmhHmUEubcFeDSoMgUEubcefbrEFnTaHtdBSiaEAmzUQpgMbDQcSpsnPpgMbDbqbEsnPpcmHNHLZDFRsiLqFAQSnfMbZFQsPHtZuIDAFoITbqSgzbMbZFfHfZzUQpHMQqbqbEpUPLtCuRPqVOAgPUHLZDcmHNnzSvEzEemNpvQcSpistEcmHNanOzEzEepUPLITbqmNpvqOZbcefbqDvcSoMgqqIuTaHtNovufHfZrseHEzEeQcSpqOZbpGbOHLZDbVauqDvceRQqUnBuqqIugsNpbZPaItQTfHfZITbqMbZFbVaunzSvQCfHNFMBiSQgSgzbcefbvGPmistEUEubgsNpozRilzvgQcSpvipdoBgpaUafgMbDITbqAhurvQCmtZuIpZzcanOzrseHTNsCFQZglzvgorCfeNnnVqrzvipdHMQqQsPHTaHtTNsCrseHRzVGcFeDMLlgLqFASgzbQBPMcFeDmOECorCfFQZgistEMbZFcFeDTNsCTaHtfHfZVuhATNsCgMbDQcSpgsNpauTzetQeReshaUafNovuvipdPqVOmgGDrEFneRQqistEMbZFFQZghcorZqdeiplPrEFnMLhbpGbOvipdQcSpZmmNoBgpgsNpfHfZaEAmLqFAMLhbSgzbQsLzHLZDozRiistEEzEemPptNovuqqIuItQTQsLzmPptQCfHhcormPptpZzcVuhAcmHNZqdeAgPUzUQpBaPPVuhAnzSvQsLzvGPmQsLzTaHtqqIuorCfaUafTNsCtCuRiSQgBaPPaEAmanOzMLhbItQTSgzbzTIhMLlgqqIuENBRanOzGdLCHLZDtCuRITbqVqrzZmmNRzVGTNsCiplPEzEeatrtDAFoMLhbbqbEauTztCuRozRirEFnReshHMQqqOZbaEAmTaHtAhurZqdeItQTaoPQpGbOtCuRLqFATNsCbqbEHLZDqOZboBgptCuRiplPetQemPptcefbistEbZPaVqrzQsLzorCfVqrzmNpvMLhbEzEeItQTNovuReshQcSpdBSiTaHtlzvgBaPPSgzbistETNsCiplPSoMgetQeLqFAbqbErseHITbqvGPmauTzFRsipUPLlzvgatrtlzvgmOECtCuRhcorqqIumgGDDAFooBgpVuhAeRQqqqIuLqFAMbZFGdLCmgGDMLlgqOZbQcSpfHfZzTIhaEAmatrtUnBuNEScMbZFeNnnbqbEMLlgTNsCUnBuqDvcqqIuozRiAhuristEAhur")
    
  expected = ["Novu", "MbZF", "Sgzb", "cmHN", "QcSp", "mPpt", "tCuR", "vQCm", "EzEe", "gsNp",
      "qqIu", "bZPa", "snPp", "ozRi", "anOz", "bVau", "NFMB", "lzvg", "tZuI", "ENBR", "iplP", 
      "HLZD", "orCf", "HMQq", "TNsC", "MLhb", "zUQp", "nzSv", "pZzc", "eNnn", "Resh", "dBSi", 
      "Zqde", "LqFA", "oBgp", "gMbD", "istE", "cFeD", "UnBu", "TaHt", "RzVG", "vGPm", "mOEC", 
      "AgPU", "QBPM", "mgGD", "BaPP", "DAFo", "SoMg", "QSnf", "UEub", "MLlg", "QCfH", "VuhA", 
      "eRQq", "aoPQ", "cefb", "zTIh", "ITbq", "Ahur", "qOZb", "vipd", "pUPL", "GdLC", "hcor", 
      "auTz", "bqbE", "aUaf", "ItQT", "pGbO", "iSQg", "qDvc", "atrt", "FRsi", "rseH", "Vqrz", 
      "mhHm", "NESc", "rEFn", "aEAm", "QsPH", "fHfZ", "QsLz", "ZmmN", "ecfi", "PqVO", "FQZg", 
      "DNiO", "mNpv", "etQe"]
  print(res[0] == expected)
  print(res[1] == "TNsC")

test()