from ROOT import TFile,TH1F,TH2F,TCanvas

hitmapFile = TFile("data15_hi.00287382.calibration_SCTNoise.sctcal.HITMAP.c0._0002.SCTHitMaps.root");
outFile = TFile("output.root","recreate")
listEA = hitmapFile.GetDirectory("SCTEA").GetListOfKeys()
listB  = hitmapFile.GetDirectory("SCTB").GetListOfKeys()
listEC = hitmapFile.GetDirectory("SCTEC").GetListOfKeys()

listOfNamesBarrel = []
counter = 0
for key in listB:
    keyName = key.GetName()
    if '2D' in keyName:
        H2D = TH2F(hitmapFile.Get("SCTB/"+keyName))
        H2D.Scale(1e-4)
        firstBin = H2D.FindFirstBinAbove(0.015)
        if (firstBin != -1):
#            print keyName
#            H2D.SetMinimum(0.010)
            c = TCanvas()
            c.SetTitle(H2D.GetTitle())
            H2D.Draw("col4z");
            c.Write("c"+str(counter))
            counter+=1
#            listOfNamesBarrel.append(keyName)

#print listOfNamesBarrel
