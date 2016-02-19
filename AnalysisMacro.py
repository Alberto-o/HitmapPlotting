from ROOT import TFile,TH1I,TH1F,TH2F,TCanvas

# hitmapFile = TFile("data15_hi.00287382.calibration_SCTNoise.sctcal.HITMAP.c0._0002.SCTHitMaps.root");
# outFile = TFile("outputhm.root","recreate")
# listEAhm = hitmapFile.GetDirectory("SCTEA").GetListOfKeys()
# listBhm  = hitmapFile.GetDirectory("SCTB").GetListOfKeys()
# listEChm = hitmapFile.GetDirectory("SCTEC").GetListOfKeys()

# listOfNamesBarrel = []
# counter = 0
# for key in listBhm:
#     keyName = key.GetName()
#     if '2D' in keyName:
#         H2D = TH2F(hitmapFile.Get("SCTB/"+keyName))
#         H2D.Scale(1e-4)
#         firstBin = H2D.FindFirstBinAbove(0.015)
#         if (firstBin != -1):
# #            print keyName
# #            H2D.SetMinimum(0.010)
#             c = TCanvas()
#             c.SetTitle(H2D.GetTitle())
#             H2D.Draw("col4z");
#             c.Write("c"+str(counter))
#             counter+=1
# #            listOfNamesBarrel.append(keyName)

#print listOfNamesBarrel
lbFile = TFile("data15_hi.00287382.calibration_SCTNoise.sctcal.HITMAP.c0._0002.SCTLB.root");
outFile = TFile("outputlb.root","recreate")
listEAlb = lbFile.GetDirectory("SCTEA").GetListOfKeys()
listBlb  = lbFile.GetDirectory("SCTB").GetListOfKeys()
listEClb = lbFile.GetDirectory("SCTEC").GetListOfKeys()

#create 1D>2D with number of events per lumiblock
eventsLB = TH1I(lbFile.Get("GENERAL/events"))
LB2D = TH2F(lbFile.Get("SCTB/0_0_0_1_0__2D"))
LB2D.Reset()
#nbinsY = LB2D.GetNbinsY()
#nbinsX = LB2D.GetNbinsX()

for binsX in range(1,eventsLB.GetNbinsX()+1):
    nLB = eventsLB.GetBinContent(binsX)
    binY = eventsLB.GetBinCenter(binsX)
    for binsX2D in range(1,LB2D.GetNbinsX()+1):
        binX = LB2D.GetXaxis().GetBinCenter(binsX2D)
        LB2D.Fill(binX,binY,nLB)
  


    # binY = LB2D.GetYaxis().GetBinCenter(binsY)
    # binYLB = eventsLB.FindBin(binY)
    # nevents = eventsLB.GetBinContent(binYLB)
    #     binX = LB2D.GetXaxis().GetBinCenter(binsX)
    #     LB2D.Fill(binX,binY,nevents)

#LB2D.RebinY(30)        
# meanEVLB = eventsLB.GetMean()
# #number of LB bins that will have roughly 10000 events
# rebinIdx = int(10000./meanEVLB)

LB2D.Write("LB2D")
eventsLB.Write("LB")
listOfNamesBarrelLB = []
counter = 0
for key in listBlb:
    keyName = key.GetName()
    if '2D' in keyName:
        H2D = TH2F(lbFile.Get("SCTB/"+keyName))
#        H2D.RebinY(30)
        H2D.Divide(LB2D)
        firstBin = H2D.FindFirstBinAbove(0.015)
        if (firstBin != -1):
            H2D.SetMinimum(0.015)                                                              
            
            c = TCanvas()
            c.SetTitle(H2D.GetTitle())
            H2D.Draw("col4z");
            c.Write("c"+str(counter))
            counter+=1
