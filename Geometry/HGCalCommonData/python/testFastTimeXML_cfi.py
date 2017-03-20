import FWCore.ParameterSet.Config as cms

# This config was generated automatically using generate2023Geometry.py
# If you notice a mistake, please update the generating script, not just this config

XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring(
        'Geometry/CMSCommonData/data/materials.xml',
        'Geometry/CMSCommonData/data/rotations.xml',
        'Geometry/CMSCommonData/data/extend/cmsextent.xml',
        'Geometry/CMSCommonData/data/cms/2023/v1/cms.xml',
        'Geometry/CMSCommonData/data/eta3/etaMax.xml',
        'Geometry/CMSCommonData/data/cmsMother.xml',
        'Geometry/CMSCommonData/data/cmsTracker.xml',
        'Geometry/CMSCommonData/data/caloBase/2023/v1/caloBase.xml',
        'Geometry/CMSCommonData/data/cmsCalo.xml',
        'Geometry/CMSCommonData/data/muonBase/2023/v1/muonBase.xml',
        'Geometry/CMSCommonData/data/cmsMuon.xml',
        'Geometry/CMSCommonData/data/mgnt.xml',
        'Geometry/CMSCommonData/data/beampipe/2023/v1/beampipe.xml',
        'Geometry/CMSCommonData/data/cmsBeam/2023/v1/cmsBeam.xml',
        'Geometry/CMSCommonData/data/muonMB.xml',
        'Geometry/CMSCommonData/data/muonMagnet.xml',
        'Geometry/CMSCommonData/data/cavern.xml',
        'Geometry/TrackerCommonData/data/trackerParameters.xml',
        'Geometry/TrackerCommonData/data/pixfwdCommon.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdMaterials.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdCylinder.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwd.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdDisks.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdInnerDisk1.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdInnerDisk2.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdInnerDisk3.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdInnerDisk4.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdInnerDisk5.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdInnerDisk6.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdInnerDisk7.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdOuterDisk1.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdOuterDisk2.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdOuterDisk3.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdOuterDisk4.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdOuterDisk5.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdOuterDisk6.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdOuterDisk7.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdOuterDisk8.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdOuterDisk9.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdOuterDisk10.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdblade1.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdblade2.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdblade3.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdblade4.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdblade5.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdblade6.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdblade7.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdblade8.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdblade9.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixfwdblade10.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarmaterial.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarladder.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull0.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull1.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull2.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull3.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer0.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer1.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer2.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer3.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/pixbar.xml',
        'Geometry/TrackerCommonData/data/trackermaterial.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/tracker.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/trackerbar.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/trackerfwd.xml',
        'Geometry/TrackerCommonData/data/TiltedTracker/trackerStructureTopology.xml',
        'Geometry/TrackerSimData/data/TiltedTracker/trackersens.xml',
        'Geometry/TrackerRecoData/data/TiltedTracker/trackerRecoMaterial.xml',
        'Geometry/TrackerSimData/data/TiltedTracker/trackerProdCuts.xml',
        'Geometry/TrackerSimData/data/trackerProdCutsBEAM.xml',
        'Geometry/EcalCommonData/data/ectkcable.xml',
        'Geometry/EcalCommonData/data/eregalgo.xml',
        'Geometry/EcalCommonData/data/ebalgo.xml',
        'Geometry/EcalCommonData/data/ebcon.xml',
        'Geometry/EcalCommonData/data/ebrot.xml',
        'Geometry/EcalCommonData/data/eecon.xml',
        'Geometry/EcalCommonData/data/escon.xml',
        'Geometry/EcalCommonData/data/esalgo.xml',
        'Geometry/HcalCommonData/data/hcalrotations.xml',
        'Geometry/HcalCommonData/data/HGCal/hcalalgo.xml',
        'Geometry/HcalCommonData/data/hcalbarrelalgo.xml',
        'Geometry/HcalCommonData/data/HGCal/hcalendcapalgo.xml',
        'Geometry/HcalCommonData/data/hcalouteralgo.xml',
        'Geometry/HcalCommonData/data/hcalforwardalgo.xml',
        'Geometry/HcalCommonData/data/hcalSimNumbering.xml',
        'Geometry/HcalCommonData/data/hcalRecNumberingRebuild.xml',
        'Geometry/HcalCommonData/data/average/hcalforwardmaterial.xml',
        'Geometry/HGCalCommonData/data/v7/hgcal.xml',
        'Geometry/HGCalCommonData/data/v7/hgcalEE.xml',
        'Geometry/HGCalCommonData/data/v7/hgcalHEsil.xml',
        'Geometry/HGCalCommonData/data/v7/hgcalwafer.xml',
        'Geometry/HGCalCommonData/data/v7/hgcalCons.xml',
        'Geometry/MuonCommonData/data/v1/mbCommon.xml',
        'Geometry/MuonCommonData/data/v1/mb1.xml',
        'Geometry/MuonCommonData/data/v1/mb2.xml',
        'Geometry/MuonCommonData/data/v1/mb3.xml',
        'Geometry/MuonCommonData/data/v1/mb4.xml',
        'Geometry/MuonCommonData/data/design/muonYoke.xml',
        'Geometry/MuonCommonData/data/mf.xml',
        'Geometry/MuonCommonData/data/rpcf.xml',
        'Geometry/MuonCommonData/data/gemf.xml',
        'Geometry/MuonCommonData/data/TDR_BaseLine/gem11.xml',
        'Geometry/MuonCommonData/data/TDR_BaseLine/gem21.xml',
        'Geometry/MuonCommonData/data/v2/csc.xml',
        'Geometry/MuonCommonData/data/mfshield.xml',
        'Geometry/MuonCommonData/data/TDR_BaseLine/me0.xml',
        'Geometry/ForwardCommonData/data/v2/forwardshield.xml',
        'Geometry/ForwardCommonData/data/brmrotations.xml',
        'Geometry/ForwardCommonData/data/PostLS2/brm.xml',
        'Geometry/ForwardCommonData/data/zdcmaterials.xml',
        'Geometry/ForwardCommonData/data/lumimaterials.xml',
        'Geometry/ForwardCommonData/data/zdcrotations.xml',
        'Geometry/ForwardCommonData/data/lumirotations.xml',
        'Geometry/ForwardCommonData/data/zdc.xml',
        'Geometry/ForwardCommonData/data/zdclumi.xml',
        'Geometry/ForwardCommonData/data/cmszdc.xml',
        'Geometry/HGCalCommonData/data/fastTimingBarrel.xml',
        'Geometry/HGCalCommonData/data/fastTimingEndcap.xml',
        'Geometry/HGCalCommonData/data/fastTimingElement.xml',
    )+
    cms.vstring(
        'Geometry/MuonCommonData/data/muonNumbering.xml',
        'Geometry/EcalSimData/data/ecalsens.xml',
        'Geometry/HcalCommonData/data/HGCal/hcalsenspmf.xml',
        'Geometry/HcalSimData/data/hf.xml',
        'Geometry/HcalSimData/data/hfpmt.xml',
        'Geometry/HcalSimData/data/hffibrebundle.xml',
        'Geometry/HcalSimData/data/CaloUtil.xml',
        'Geometry/HGCalSimData/data/hgcsensv6.xml',
        'Geometry/HGCalSimData/data/hgccons.xml',
        'Geometry/HGCalSimData/data/hgcProdCuts.xml',
        'Geometry/MuonSimData/data/muonSens.xml',
        'Geometry/DTGeometryBuilder/data/dtSpecsFilter.xml',
        'Geometry/CSCGeometryBuilder/data/cscSpecsFilter.xml',
        'Geometry/CSCGeometryBuilder/data/cscSpecs.xml',
        'Geometry/RPCGeometryBuilder/data/RPCSpecs.xml',
        'Geometry/GEMGeometryBuilder/data/GEMSpecsFilter.xml',
        'Geometry/GEMGeometryBuilder/data/v5/GEMSpecs.xml',
        'Geometry/ForwardCommonData/data/brmsens.xml',
        'Geometry/ForwardSimData/data/zdcsens.xml',
        'Geometry/HGCalSimData/data/fasttimesens.xml',
        'Geometry/HcalSimData/data/HcalProdCuts.xml',
        'Geometry/EcalSimData/data/EcalProdCuts.xml',
        'Geometry/MuonSimData/data/muonProdCuts.xml',
        'Geometry/ForwardSimData/data/zdcProdCuts.xml',
        'Geometry/ForwardSimData/data/ForwardShieldProdCuts.xml',
        'Geometry/HGCalSimData/data/fasttimeProdCuts.xml',
        'Geometry/CMSCommonData/data/FieldParameters.xml',
    ),
    rootNodeName = cms.string('cms:OCMS')
)
