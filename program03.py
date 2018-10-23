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

tot_time = .0

def find_words_in_string(words, string_to_process):
  seen_words, seen_words_n = ({}, {})
  chunk_size = 50
  chunks = []
  for i in range(0, len(string_to_process) // chunk_size + 1):
    chunks.append(string_to_process[i * chunk_size: i * chunk_size + chunk_size])
  last_percent_printed = .0
  percentage_sensitivity = 1
  leftover = ""

  print("Starting to process", len(chunks), "chunks")
  for i in range(0, len(chunks)):
    #Percentage
    percent_done = i / len(chunks) * 100
    if percent_done - last_percent_printed >= percentage_sensitivity:
      last_percent_printed = percent_done
      print("Chunks done...", percent_done, "%")

    #Actual processing
    string = leftover + chunks[i]
    leftover = processChunk(words, string, seen_words, seen_words_n)
        
  return (seen_words, seen_words_n)

def processChunk(words_dict, string, seen_words, seen_words_n):
  global tot_time #Benchmark
  
  while len(string) > 0:
    word = getMatchingWordFromDict(words_dict, string)
    if word == None:
      break
    else:
      start_time = time.time() #Benchmark Start
      if word[0] not in seen_words:
        seen_words[word[0]] = []
      if word not in seen_words[word[0]]:
        seen_words[word[0]].append(word)
        seen_words_n[word] = 1
      else:
        seen_words_n[word] += 1
      tot_time += time.time() - start_time #Benchmark End
      string = string[len(word):] #Slow part
  return(string)

def getMatchingWord(words, string):
  matching_word = None
  for word in words:

    if len(word) > len(string):
      continue

    matching = word == string[0:len(word)]

    if matching:
      matching_word = word
      break

  return matching_word

def getMatchingWordFromDict(words_dict, string):

  matching_word = None
  words_to_check = words_dict[string[0]]
  matching_word = getMatchingWord(words_to_check, string)
    
  return matching_word
  
def getMostCommonWord(words_dict, occurances):
  print(occurances)
  print(words_dict)
  max_word_occurances = 0
  for occurance in occurances:
    if occurances[occurance] > max_word_occurances:
      max_word_occurances = occurances[occurance]
  most_common_words = []
  for words_key in words_dict:
    for word in words_dict[words_key]:
      if occurances[word] == max_word_occurances:
        most_common_words.append(word)

  repeating_word = sorted(most_common_words, key=lambda word: word[0])[0]
  return repeating_word

def addToDict(string, dict):
  char = string[0]
  if char not in dict:
    dict[char] = {}
  if len(string) > 1:
    addToDict(string[1:], dict[char])

def es3(lista, testo):

  words_dict = {}

  for word in lista:
    if word[0] not in words_dict:
      words_dict[word[0]] = []
    words_dict[word[0]].append(word)

  seen_words, seen_words_n = find_words_in_string(words_dict, testo)
  most_common_word = getMostCommonWord(seen_words, seen_words_n)

  for word_key in seen_words:
    for word in seen_words[word_key]:
      lista.remove(word)

  resulting_words = []
  for words_key in seen_words:
    for word in seen_words[words_key]:
      # print(word)
      resulting_words.append(word)
  print(resulting_words)

  print("Tot_time", tot_time)

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