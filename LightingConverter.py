import sys
import math
import xml.etree.ElementTree as ET

FLOAT_LIGHTING_TYPES = {
    "mipmapbias": "cXSLightingMipMapBias",
    "sunintensity": "cXSLightingSunIntensity",
    "skyintensity": "cXSLightingSkyIntensity",
    "skyturbidity": "cXSLightingSkyTurbidity",
    "contactshadowintensity": "cXSLightingContactShadowIntensity",
    "bloomthreshold": "cXSLightingBloomThreshold",
    "bloomintensity": "cXSLightingBloomIntensity",
    "bloomcrunching": "cXSLightingBloomCrunching",
    "exposure": "cXSLightingExposure",
    "emissiveexposure": "cXSLightingEmissiveExposure",
    "whitepoint": "cXSLightingWhitePoint",
    "displaygamma": "cXSLightingDisplayGamma",
    "displaybrightness": "cXSLightingDisplayBrightness",
    "dithernoiseintensity": "cXSLightingDitherNoiseIntensity",
    "tonemapluminance": "cXSLightingTonemapLuminance",
    "tonemapinfluence": "cXSLightingTonemapInfluence",
    "shadowsoftness": "cXSLightingShadowSoftness",
    "aointensity": "cXSLightingAOIntensity",
    "heightbasedlightcurve": "cXSLightingHeightBasedLightCurve",
    "heightbasedlightintensity": "cXSLightingHeightBasedLightIntensity",
    "giheight": "cXSLightingGIHeight",
    "gipower": "cXSLightingGIPower",
    "giintensity": "cXSLightingGIIntensity",
    "heightfogtop": "cXSLightingHeightFogTop",
    "heightfogbottom": "cXSLightingHeightFogBottom",
    "heightfogstartfalloff": "cXSLightingHeightFogStartFalloff",
    "heightfogdensity": "cXSLightingHeightFogDensity",
    "distancefogdensityclose": "cXSLightingDistanceFogDensityClose",
    "distancefogclose": "cXSLightingDistanceFogClose",
    "distancefogdensityfar": "cXSLightingDistanceFogDensityFar",
    "distancefogfar": "cXSLightingDistanceFogFar",
    "colorgradeintensity": "cXSLightingColorGradeIntensity",
    "colorgradehue_global": "cXSLightingColorGradeHue_Global",
    "colorgradehue_shadows": "cXSLightingColorGradeHue_Shadows",
    "colorgradehue_midtones": "cXSLightingColorGradeHue_Midtones",
    "colorgradehue_highlights": "cXSLightingColorGradeHue_Highlights",
    "colorgradesaturation_global": "cXSLightingColorGradeSaturation_Global",
    "colorgradesaturation_shadows": "cXSLightingColorGradeSaturation_Shadows",
    "colorgradesaturation_midtones": "cXSLightingColorGradeSaturation_Midtones",
    "colorgradesaturation_highlights": "cXSLightingColorGradeSaturation_Highlights"
}

FLOAT_ROTATION_LIGHTING_TYPES = {
    "suninclination": "cXSLightingSunInclination",
    "sunrotation": "cXSLightingSunRotation"
}

INT_LIGHTING_TYPES = {
    "bloomiterations": "cXSLightingBloomIterations",
    "aotype": "cXSLightingAOType"
}

BOOL_LIGHTING_TYPES = {
    "aoinshadowsonly": "cXSLightingAOInShadowsOnly",
    "heightfogenabled": "cXSLightingHeightFogEnabled",
    "distancefogenabled": "cXSLightingDistanceFogEnabled"
}

COLOUR_INT_LIGHTING_TYPES = {
    "suntint": "cXSLightingSunTint",
    "shadowcolor": "cXSLightingShadowColor",
    "bloomtint": "cXSLightingBloomTint",
    "heightfogcolor": "cXSLightingHeightFogColor",
    "distancefogcolor": "cXSLightingDistanceFogColor",
}
COLOUR_CONVERT_TO_INT_LIGHTING_TYPES = {
    "colorgradetint_global": "cXSLightingColorGradeTint_Global",
    "colorgradetint_shadows": "cXSLightingColorGradeTint_Shadows",
    "colorgradetint_midtones": "cXSLightingColorGradeTint_Midtones",
    "colorgradetint_highlights": "cXSLightingColorGradeTint_Highlights",
    "colorgradeoffset_global": "cXSLightingColorGradeOffset_Global",
    "colorgradeoffset_shadows": "cXSLightingColorGradeOffset_Shadows",
    "colorgradeoffset_midtones": "cXSLightingColorGradeOffset_Midtones",
    "colorgradeoffset_highlights": "cXSLightingColorGradeOffset_Highlights",
}

COLOUR_ATTRIBUTE_LIGHTING_TYPES = {
    "colorgradegain": "cXSLightingColorGradeGain",
    "colorgradegamma": "cXSLightingColorGradeGamma",
    "colorgradecontrast": "cXSLightingColorGradeContrast",
}

def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

def is_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

def main(file):
    tree = ET.parse(file)
    root = tree.getroot()
    index = 0
    print('PASTE PART 1')
    for child in root:
        data = child.text
        tagName = child.tag
        if data == None:
            pass
        elif tagName in FLOAT_LIGHTING_TYPES:
            print('trLightingSetParamFloat('+FLOAT_LIGHTING_TYPES[tagName]+', '+str(data)+');')
        elif tagName in FLOAT_ROTATION_LIGHTING_TYPES:
            print('trLightingSetParamFloat('+FLOAT_ROTATION_LIGHTING_TYPES[tagName]+', '+str(math.radians(float(data)))+');')
        elif tagName in INT_LIGHTING_TYPES:
            print('trLightingSetParamInt('+INT_LIGHTING_TYPES[tagName]+', '+str(data)+');')
        elif tagName in BOOL_LIGHTING_TYPES:
            print('trLightingSetParamBool('+BOOL_LIGHTING_TYPES[tagName]+', '+('true' if data == '1' else 'false')+');')
        elif tagName in COLOUR_INT_LIGHTING_TYPES:
            parts = data.split(' ')
            print('trLightingSetParamColor('+COLOUR_INT_LIGHTING_TYPES[tagName]+', '+str(parts[0])+', '+str(parts[1])+', '+str(parts[2])+');')
        elif tagName in COLOUR_CONVERT_TO_INT_LIGHTING_TYPES:
            parts = data.split(', ')
            print('trLightingSetParamColor('+COLOUR_CONVERT_TO_INT_LIGHTING_TYPES[tagName]+', '+str(round(float(parts[0]) * 255))+', '+str(round(float(parts[1]) * 255))+', '+str(round(float(parts[2]) * 255))+');')
        elif tagName in COLOUR_ATTRIBUTE_LIGHTING_TYPES:
            parts = data.split(', ')
            print('trLightingSetParamColorAttr('+COLOUR_ATTRIBUTE_LIGHTING_TYPES[tagName]+', '+str(parts[0])+', '+str(parts[1])+', '+str(parts[2])+');')
        index = index + 1
        if index == 35:
            print('PASTE PART 2')  
    SystemExit()
    
    
if __name__ == "__main__":
    if len(sys.argv) < 1:
        print('No filename was provided to parse. Please provide the filename as the first argument.')
        SystemExit()
    main(sys.argv[1])