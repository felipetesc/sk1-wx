# 
#
#  Copyright (C) = 2019 by Maxim S. Barabash
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version = 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https:#www.gnu.org/licenses/>.


from uc2.uc2const import COLOR_RGB, COLOR_CMYK, COLOR_GRAY


XAR_SIGNATURE = b'XARA\xa3\xa3\r\n'


CO_ORDINATES_DPI = 72000.0

# Navigation records
TAG_UP = 0
TAG_DOWN = 1
TAG_FILEHEADER = 2
TAG_ENDOFFILE = 3

# Tag management
TAG_ATOMICTAGS = 10
TAG_ESSENTIALTAGS = 11
TAG_TAGDESCRIPTION = 12

# Compression tags
TAG_STARTCOMPRESSION = 30
TAG_ENDCOMPRESSION = 31

# Document tags
TAG_DOCUMENT = 40
TAG_CHAPTER = 41
TAG_SPREAD = 42

# Notes

TAG_LAYER = 43
TAG_PAGE = 44
TAG_SPREADINFORMATION = 45
TAG_GRIDRULERSETTINGS = 46
TAG_GRIDRULERORIGIN = 47
TAG_LAYERDETAILS = 48
TAG_GUIDELAYERDETAILS = 49
TAG_SPREADSCALING_ACTIVE = 52
TAG_SPREADSCALING_INACTIVE = 53

# Colour reference tags
TAG_DEFINERGBCOLOUR = 50
TAG_DEFINECOMPLEXCOLOUR = 51

# Bitmap reference tags
TAG_RESERVED_60 = 60
TAG_PREVIEWBITMAP_GIF = 61
TAG_PREVIEWBITMAP_JPEG = 62
TAG_PREVIEWBITMAP_PNG = 63
TAG_RESERVED_64 = 64
TAG_RESERVED_65 = 65
TAG_RESERVED_66 = 66
TAG_DEFINEBITMAP_JPEG = 67
TAG_DEFINEBITMAP_PNG = 68
TAG_RESERVED_69 = 69
TAG_RESERVED_70 = 70
TAG_DEFINEBITMAP_JPEG8BPP = 71

# View tags
TAG_VIEWPORT = 80
TAG_VIEWQUALITY = 81
TAG_DOCUMENTVIEW = 82

# Document unit tags
TAG_DEFINE_PREFIXUSERUNIT = 85
TAG_DEFINE_SUFFIXUSERUNIT = 86
TAG_DEFINE_DEFAULTUNITS = 87

# Document info tags
TAG_DOCUMENTCOMMENT = 90
TAG_DOCUMENTDATES = 91
TAG_DOCUMENTUNDOSIZE = 92
TAG_DOCUMENTFLAGS = 93
TAG_DOCUMENTINFORMATION = 4136

# Object tags
TAG_PATH = 100
TAG_PATH_FILLED = 101
TAG_PATH_STROKED = 102
TAG_PATH_FILLED_STROKED = 103
TAG_GROUP = 104
TAG_BLEND = 105
TAG_BLENDER = 106
TAG_MOULD_ENVELOPE = 107
TAG_MOULD_PERSPECTIVE = 108
TAG_MOULD_GROUP = 109
TAG_MOULD_PATH = 110
TAG_PATH_FLAGS = 111
TAG_GUIDELINE = 112
TAG_PATH_RELATIVE = 113
TAG_PATH_RELATIVE_FILLED = 114
TAG_PATH_RELATIVE_STROKED = 115
TAG_PATH_RELATIVE_FILLED_STROKED = 116
TAG_RESERVED_117 = 117
TAG_PATHREF_TRANSFORM = 118

# Attribute tags
TAG_FLATFILL = 150
TAG_LINECOLOUR = 151
TAG_LINEWIDTH = 152
TAG_LINEARFILL = 153
TAG_CIRCULARFILL = 154
TAG_ELLIPTICALFILL = 155
TAG_CONICALFILL = 156
TAG_BITMAPFILL = 157
TAG_CONTONEBITMAPFILL = 158
TAG_FRACTALFILL = 159
TAG_FILLEFFECT_FADE = 160
TAG_FILLEFFECT_RAINBOW = 161
TAG_FILLEFFECT_ALTRAINBOW = 162
TAG_FILL_REPEATING = 163
TAG_FILL_NONREPEATING = 164
TAG_FILL_REPEATINGINVERTED = 165
TAG_FLATTRANSPARENTFILL = 166
TAG_LINEARTRANSPARENTFILL = 167
TAG_CIRCULARTRANSPARENTFILL = 168
TAG_ELLIPTICALTRANSPARENTFILL = 169
TAG_CONICALTRANSPARENTFILL = 170
TAG_BITMAPTRANSPARENTFILL = 171
TAG_FRACTALTRANSPARENTFILL = 172
TAG_LINETRANSPARENCY = 173
TAG_STARTCAP = 174
TAG_ENDCAP = 175
TAG_JOINSTYLE = 176
TAG_MITRELIMIT = 177
TAG_WINDINGRULE = 178
TAG_QUALITY = 179
TAG_TRANSPARENTFILL_REPEATING = 180
TAG_TRANSPARENTFILL_NONREPEATING = 181
TAG_TRANSPARENTFILL_REPEATINGINVERTED = 182

# Arrows and dash patterns
TAG_DASHSTYLE = 183
TAG_DEFINEDASH = 184
TAG_ARROWHEAD = 185
TAG_ARROWTAIL = 186
TAG_DEFINEARROW = 187
TAG_DEFINEDASH_SCALED = 188

# User Attributes
TAG_USERVALUE = 189

# special colour fills
TAG_FLATFILL_NONE = 190
TAG_FLATFILL_BLACK = 191
TAG_FLATFILL_WHITE = 192
TAG_LINECOLOUR_NONE = 193
TAG_LINECOLOUR_BLACK = 194
TAG_LINECOLOUR_WHITE = 195

# Bitmaps
TAG_NODE_BITMAP = 198
TAG_NODE_CONTONEDBITMAP = 199

# New fill type records
TAG_DIAMONDFILL = 200
TAG_DIAMONDTRANSPARENTFILL = 201
TAG_THREECOLFILL = 202
TAG_THREECOLTRANSPARENTFILL = 203
TAG_FOURCOLFILL = 204
TAG_FOURCOLTRANSPARENTFILL = 205
TAG_FILL_REPEATING_EXTRA = 206
TAG_TRANSPARENTFILL_REPEATING_EXTRA = 207

# Regular shapes
# Ellipses
TAG_ELLIPSE_SIMPLE = 1000
TAG_ELLIPSE_COMPLEX = 1001

# Rectangles
TAG_RECTANGLE_SIMPLE = 1100
TAG_RECTANGLE_SIMPLE_REFORMED = 1101  # Deprecated
TAG_RECTANGLE_SIMPLE_STELLATED = 1102  # Deprecated
TAG_RECTANGLE_SIMPLE_STELLATED_REFORMED = 1103  # Deprecated
TAG_RECTANGLE_SIMPLE_ROUNDED = 1104
TAG_RECTANGLE_SIMPLE_ROUNDED_REFORMED = 1105  # Deprecated
TAG_RECTANGLE_SIMPLE_ROUNDED_STELLATED = 1106  # Deprecated
TAG_RECTANGLE_SIMPLE_ROUNDED_STELLATED_REFORMED = 1107  # Deprecated
TAG_RECTANGLE_COMPLEX = 1108
TAG_RECTANGLE_COMPLEX_REFORMED = 1109  # Deprecated
TAG_RECTANGLE_COMPLEX_STELLATED = 1110  # Deprecated
TAG_RECTANGLE_COMPLEX_STELLATED_REFORMED = 1111  # Deprecated
TAG_RECTANGLE_COMPLEX_ROUNDED = 1112
TAG_RECTANGLE_COMPLEX_ROUNDED_REFORMED = 1113  # Deprecated
TAG_RECTANGLE_COMPLEX_ROUNDED_STELLATED = 1114  # Deprecated
TAG_RECTANGLE_COMPLEX_ROUNDED_STELLATED_REFORMED = 1115  # Deprecated

# Polygons
TAG_POLYGON_COMPLEX = 1200
TAG_POLYGON_COMPLEX_REFORMED = 1201  # Deprecated
TAG_POLYGON_COMPLEX_STELLATED = 1212  # Deprecated
TAG_POLYGON_COMPLEX_STELLATED_REFORMED = 1213  # Deprecated
TAG_POLYGON_COMPLEX_ROUNDED = 1214
TAG_POLYGON_COMPLEX_ROUNDED_REFORMED = 1215
TAG_POLYGON_COMPLEX_ROUNDED_STELLATED = 1216
TAG_POLYGON_COMPLEX_ROUNDED_STELLATED_REFORMED = 1217  # Deprecated

# General regular shapes
TAG_REGULAR_SHAPE_PHASE_1 = 1900
TAG_REGULAR_SHAPE_PHASE_2 = 1901

# Text related records
# Text definitions
TAG_FONT_DEF_TRUETYPE = 2000
TAG_FONT_DEF_ATM = 2001

# vanilla text story objects
TAG_TEXT_STORY_SIMPLE = 2100
TAG_TEXT_STORY_COMPLEX = 2101

# text story objects on a path
TAG_TEXT_STORY_SIMPLE_START_LEFT = 2110
TAG_TEXT_STORY_SIMPLE_START_RIGHT = 2111
TAG_TEXT_STORY_SIMPLE_END_LEFT = 2112
TAG_TEXT_STORY_SIMPLE_END_RIGHT = 2113
TAG_TEXT_STORY_COMPLEX_START_LEFT = 2114
TAG_TEXT_STORY_COMPLEX_START_RIGHT = 2115
TAG_TEXT_STORY_COMPLEX_END_LEFT = 2116  # Deprecated
TAG_TEXT_STORY_COMPLEX_END_RIGHT = 2117

# Text story information records
TAG_TEXT_STORY_WORD_WRAP_INFO = 2150
TAG_TEXT_STORY_INDENT_INFO = 2151

# other text story related objects
TAG_TEXT_LINE = 2200
TAG_TEXT_STRING = 2201
TAG_TEXT_CHAR = 2202
TAG_TEXT_EOL = 2203
TAG_TEXT_KERN = 2204
TAG_TEXT_CARET = 2205
TAG_TEXT_LINE_INFO = 2206

# Text attributes
TAG_TEXT_LINESPACE_RATIO = 2900
TAG_TEXT_LINESPACE_ABSOLUTE = 2901
TAG_TEXT_JUSTIFICATION_LEFT = 2902
TAG_TEXT_JUSTIFICATION_CENTRE = 2903
TAG_TEXT_JUSTIFICATION_RIGHT = 2904
TAG_TEXT_JUSTIFICATION_FULL = 2905
TAG_TEXT_FONT_SIZE = 2906
TAG_TEXT_FONT_TYPEFACE = 2907
TAG_TEXT_BOLD_ON = 2908
TAG_TEXT_BOLD_OFF = 2909
TAG_TEXT_ITALIC_ON = 2910
TAG_TEXT_ITALIC_OFF = 2911
TAG_TEXT_UNDERLINE_ON = 2912
TAG_TEXT_UNDERLINE_OFF = 2913
TAG_TEXT_SCRIPT_ON = 2914
TAG_TEXT_SCRIPT_OFF = 2915
TAG_TEXT_SUPERSCRIPT_ON = 2916
TAG_TEXT_SUBSCRIPT_ON = 2917
TAG_TEXT_TRACKING = 2918
TAG_TEXT_ASPECT_RATIO = 2919
TAG_TEXT_BASELINE = 2920

# Imagesetting attributes
TAG_OVERPRINTLINEON = 3500
TAG_OVERPRINTLINEOFF = 3501
TAG_OVERPRINTFILLON = 3502
TAG_OVERPRINTFILLOFF = 3503
TAG_PRINTONALLPLATESON = 3504
TAG_PRINTONALLPLATESOFF = 3505

# Document Print/Imagesetting options
TAG_PRINTERSETTINGS = 3506
TAG_IMAGESETTING = 3507
TAG_COLOURPLATE = 3508

# Registration mark records
TAG_PRINTMARKDEFAULT = 3509
TAG_RESERVED_3510 = 3510

# Stroking records
TAG_VARIABLEWIDTHFUNC = 4000  # This record is not currently used
TAG_VARIABLEWIDTHTABLE = 4001
TAG_STROKETYPE = 4002
TAG_STROKEDEFINITION = 4003  # This record is not currently used
TAG_STROKEAIRBRUSH = 4004  # This record is not currently used

# Fractal Noise records
TAG_NOISEFILL = 4010
TAG_NOISETRANSPARENTFILL = 4011

# Mould bounds record
TAG_MOULD_BOUNDS = 4012

# Bitmap export hint record
TAG_EXPORT_HINT = 4015

# Web Address tags
TAG_WEBADDRESS = 4020
TAG_WEBADDRESS_BOUNDINGBOX = 4021

# Frame layer tags
TAG_LAYER_FRAMEPROPS = 4030
TAG_SPREAD_ANIMPROPS = 4031

# Wizard properties tags
TAG_WIZOP = 4040
TAG_WIZOP_STYLE = 4041
TAG_WIZOP_STYLEREF = 4042

# Shadow tags
TAG_SHADOWCONTROLLER = 4050
TAG_SHADOW = 4051

# Bevel tags
TAG_BEVEL = 4052
TAG_BEVATTR_INDENT = 4053  # Deprecated
TAG_BEVATTR_LIGHTANGLE = 4054  # Deprecated
TAG_BEVATTR_CONTRAST = 4055  # Deprecated
TAG_BEVATTR_TYPE = 4056  # Deprecated
TAG_BEVELINK = 4057

# Blend on a curve tags
TAG_BLENDER_CURVEPROP = 4060
TAG_BLEND_PATH = 4061
TAG_BLENDER_CURVEANGLES = 4062

# Contouring tags
TAG_CONTOURCONTROLLER = 4066
TAG_CONTOUR = 4067

# Set tags
TAG_SETSENTINEL = 4070
TAG_SETPROPERTY = 4071

# More Blend on a curve tags
TAG_BLENDPROFILES = 4072
TAG_BLENDERADDITIONAL = 4073
TAG_NODEBLENDPATH_FILLED = 4074

# Multi stage fill tags
TAG_LINEARFILLMULTISTAGE = 4075
TAG_CIRCULARFILLMULTISTAGE = 4076
TAG_ELLIPTICALFILLMULTISTAGE = 4077
TAG_CONICALFILLMULTISTAGE = 4078

# Brush attribute tags
TAG_BRUSHATTR = 4079
TAG_BRUSHDEFINITION = 4080
TAG_BRUSHDATA = 4081
TAG_MOREBRUSHDATA = 4082
TAG_MOREBRUSHATTR = 4083

# ClipView tags
TAG_CLIPVIEWCONTROLLER = 4084
TAG_CLIPVIEW = 4085

# Feathering tags
TAG_FEATHER = 4086

# Bar properties tag
TAG_BARPROPERTY = 4087

# Other multi stage fill tags
TAG_SQUAREFILLMULTISTAGE = 4088

# More brush tags
TAG_EVENMOREBRUSHDATA = 4102
TAG_EVENMOREBRUSHATTR = 4103
TAG_TIMESTAMPBRUSHDATA = 4104
TAG_BRUSHPRESSUREINFO = 4105
TAG_BRUSHPRESSUREDATA = 4106
TAG_BRUSHATTRPRESSUREINFO = 4107
TAG_BRUSHCOLOURDATA = 4108
TAG_BRUSHPRESSURESAMPLEDATA = 4109
TAG_BRUSHTIMESAMPLEDATA = 4110
TAG_BRUSHATTRFILLFLAGS = 4111
TAG_BRUSHTRANSPINFO = 4112
TAG_BRUSHATTRTRANSPINFO = 4113

# Nudge size record
TAG_DOCUMENTNUDGE = 4114

# Bitmap properties record
TAG_BITMAP_PROPERTIES = 4115

# Bitmap smoothing record
TAG_DOCUMENTBITMAPSMOOTHING = 4116

# XPE bitmap processing record
TAG_XPE_BITMAP_PROPERTIES = 4117

# XPE Bitmap file format placeholder record
TAG_DEFINEBITMAP_XPE = 4118

# Current attributes records
TAG_CURRENTATTRIBUTES = 4119
TAG_CURRENTATTRIBUTEBOUNDS = 4120

# = 3-point linear fill records
TAG_LINEARFILL3POINT = 4121
TAG_LINEARFILLMULTISTAGE3POINT = 4122
TAG_LINEARTRANSPARENTFILL3POINT = 4123

# Duplication distance record
TAG_DUPLICATIONOFFSET = 4124

# Bitmap effect tags
TAG_LIVE_EFFECT = 4125
TAG_LOCKED_EFFECT = 4126
TAG_FEATHER_EFFECT = 4127

# Miscellaneous records
TAG_COMPOUNDRENDER = 4128
TAG_OBJECTBOUNDS = 4129
TAG_SPREAD_PHASE2 = 4131
TAG_CURRENTATTRIBUTES_PHASE2 = 4132
TAG_SPREAD_FLASHPROPS = 4134
TAG_PRINTERSETTINGS_PHASE2 = 4135
TAG_DOCUMENTINFORMATION = 4136
TAG_CLIPVIEW_PATH = 4137
TAG_DEFINEBITMAP_PNG_REAL = 4138
TAG_TEXT_STRING_POS = 4139
TAG_SPREAD_FLASHPROPS2 = 4140
TAG_TEXT_LINESPACE_LEADING = 4141

# New text records
TAG_TEXT_TAB = 4200
TAG_TEXT_LEFT_INDENT = 4201
TAG_TEXT_FIRST_INDENT = 4202
TAG_TEXT_RIGHT_INDENT = 4203
TAG_TEXT_RULER = 4204
TAG_TEXT_STORY_HEIGHT_INFO = 4205
TAG_TEXT_STORY_LINK_INFO = 4206
TAG_TEXT_STORY_TRANSLATION_INFO = 4207
TAG_TEXT_SPACE_BEFORE = 4208
TAG_TEXT_SPACE_AFTER = 4209
TAG_TEXT_SPECIAL_HYPHEN = 4210
TAG_TEXT_SOFT_RETURN = 4211
TAG_TEXT_EXTRA_FONT_INFO = 4212
TAG_TEXT_EXTRA_TT_FONT_DEF = 4213
TAG_TEXT_EXTRA_ATM_FONT_DEF = 4214

FILE_TYPE_PAPER_PUBLISH = b'CXN'
FILE_TYPE_WEB = b'CXW'


# Colors
RGB_BLACK = [COLOR_RGB, [0.0, 0.0, 0.0], 1.0, 'black']
RGB_WHITE = [COLOR_RGB, [1.0, 1.0, 1.0], 1.0, 'white']

CMYK_BLACK = [COLOR_CMYK, [0.0, 0.0, 0.0, 1.0], 1.0, 'black']
CMYK_WHITE = [COLOR_CMYK, [0.0, 0.0, 0.0, 0.0], 1.0, 'white']

GREYSCALE_BLACK = [COLOR_GRAY, [1.0], 1.0, 'black']
GREYSCALE_WHITE = [COLOR_GRAY, [0.0], 1.0, 'white']


XAR_COLOURS = {
    -1: None,
    -2: [COLOR_RGB, [0.00, 0.00, 0.00], 1.0, 'black'],
    -3: [COLOR_RGB, [1.00, 1.00, 1.00], 1.0, 'white'],
    -4: [COLOR_RGB, [1.00, 0.00, 0.00], 1.0, 'red'],
    -5: [COLOR_RGB, [0.00, 1.00, 0.00], 1.0, 'green'],
    -6: [COLOR_RGB, [0.00, 0.00, 1.00], 1.0, 'blue'],
    -7: [COLOR_CMYK, [1.00, 0.00, 0.00, 0.0], 1.0, 'cyan'],
    -8: [COLOR_CMYK, [0.00, 1.00, 0.00, 0.0], 1.0, 'magenta'],
    -9: [COLOR_CMYK, [0.00, 0.00, 1.00, 0.0], 1.0, 'yellow'],
}

# Colour models
COLOUR_MODEL_RGB = 2
COLOUR_MODEL_CMYK = 3
COLOUR_MODEL_HSV = 4
COLOUR_MODEL_GREYSCALE = 5

# Colour types
COLOUR_TYPE_NORMAL = 0
COLOUR_TYPE_SPOT = 1
COLOUR_TYPE_TINT = 2
COLOUR_TYPE_LINKED = 3
COLOUR_TYPE_SHADE = 4

# Default Units
REF_UNIT_MILLIMETRES = -2
REF_UNIT_CENTIMETRES = -3
REF_UNIT_METRES = -4
REF_UNIT_KILOMETRES = -5
REF_UNIT_MILLIPOINTS = -6
REF_UNIT_COMP_POINTS = -7
REF_UNIT_PICAS = -8
REF_UNIT_INCHES = -9
REF_UNIT_FEET = -10
REF_UNIT_YARDS = -11
REF_UNIT_MILES = -12
REF_UNIT_PIXELS = -13

# Possible values for Path Verb
PT_MOVETO = 0x6
PT_LINETO = 0x2
PT_BEZIERTO = 0x4

# Stroke props
JOIN_MITRE = 0
JOIN_ROUND = 1
JOIN_BEVEL = 2

CAP_BUTT = 0
CAP_ROUND = 1
CAP_SQUARE = 2

FILL_NONZERO = 0
FILL_EVENODD = 2

# Ref Colors
REF_DEFAULTCOLOUR_NONE = -1
REF_DEFAULTCOLOUR_BLACK = -2
REF_DEFAULTCOLOUR_WHITE = -3
REF_DEFAULTCOLOUR_RED = -4
REF_DEFAULTCOLOUR_GREEN = -5
REF_DEFAULTCOLOUR_BLUE = -6
REF_DEFAULTCOLOUR_CYAN = -7
REF_DEFAULTCOLOUR_MAGENTA = -8
REF_DEFAULTCOLOUR_YELLOW = -9


# Defaults

REF_DASH_SOLID = -21
REF_DASH_1 = -1
REF_DASH_2 = -2


XAR_DEFAULT_STYLE = {
    'mitre_limit': 4000,
    'end_arrow': None,
    'start_arrow': None,
    'start_cap': CAP_BUTT,
    'dash_pattern': REF_DASH_SOLID,
    'quality': 110,
    'join_type': JOIN_BEVEL,
    'winding_rule': FILL_EVENODD,
    'line_width': 0.501,
    'fill_effect_fade': None,
    'transp_fill_mapping_linear': None,
    'fill_mapping_linear': None,
    'flat_transp_fill': None,
    'flat_colour_fill': None,
    # 'StrokeTransp',
    'stroke_transparency': 0.0,
    'stroke_colour': RGB_WHITE,
    'feather': None,
    'stroke_type': 0x01000000,
    # addition
    'pattern_fill': None,
    'gradient_fill': None,
    'fill_repeating': None,
}


XAR_TYPE_RECORD = {

    # Navigation records
    TAG_UP: {'name': 'UP'},
    TAG_DOWN: {'name': 'DOWN'},
    TAG_FILEHEADER: {
        'name': 'FILEHEADER',
        'doc': 'This record gives useful information about the file. '
               'This should always be the first record in any file produced.',
        'sec': [
            {'type': '3 bytes', 'id': 'file_type',
                'enum': {  # XXX
                    '0': {'value': FILE_TYPE_PAPER_PUBLISH},
                    '1': {'value': FILE_TYPE_WEB}
                }
            },
            {'type': 'uint32', 'id': 'file_size'},
            {'type': 'uint32', 'id': 'web_link'},
            {'type': 'uint32', 'id': 'refinement_flags'},
            {'type': 'ASCII_STRING', 'id': 'producer'},
            {'type': 'ASCII_STRING', 'id': 'producer_version'},
            {'type': 'ASCII_STRING', 'id': 'producer_build'},
        ]
    },
    TAG_ENDOFFILE: {'name': 'ENDOFFILE'},

    # Tag management
    TAG_ATOMICTAGS: {'name': 'ATOMICTAGS'},
    TAG_ESSENTIALTAGS: {'name': 'ESSENTIALTAGS'},
    TAG_TAGDESCRIPTION: {
        'name': 'TAGDESCRIPTION',
        'sec': [
            {'type': 'uint32', 'id': 'number_of_tags'},
            {'type': 'Tag Description*', 'id': 'description'}
        ]
    },

    # Compression tags
    TAG_STARTCOMPRESSION: {
        'name': 'STARTCOMPRESSION',
        'sec': [
            {'type': '3 bytes', 'id': 'compression_version', 'encoding': 'hex'},
            {'type': 'byte', 'id': 'compression_type'},
        ]
    },
    TAG_ENDCOMPRESSION: {
        'name': 'ENDCOMPRESSION',
        'sec': [
            {'type': 'uint32', 'id': 'compression_crc'},
            {'type': 'uint32', 'id': 'num_bytes'}
        ]
    },

    # Document tags
    TAG_DOCUMENT: {'name': 'DOCUMENT'},
    TAG_CHAPTER: {'name': 'CHAPTER'},
    TAG_SPREAD: {'name': 'SPREAD'},

    # Notes

    TAG_LAYER: {'name': 'LAYER'},
    TAG_PAGE: {
        'name': 'PAGE',
        'sec': [
            {'type': 'COORD', 'id': 'bottom_left'},
            {'type': 'COORD', 'id': 'top_right'},
            {'type': 'COLOURREF', 'id': 'colour'},
        ]
    },
    TAG_SPREADINFORMATION: {
        'name': 'SPREADINFORMATION',
        'sec': [
            {'type': 'MILLIPOINT', 'id': 'width'},
            {'type': 'MILLIPOINT', 'id': 'height'},
            {'type': 'MILLIPOINT', 'id': 'margin'},
            {'type': 'MILLIPOINT', 'id': 'bleed'},
            {'type': 'byte', 'id': 'spread_flags',
                 'bitfield': {
                     0: {'type': 'bool', 'id': 'double_page_spread'},
                     1: {'type': 'bool', 'id': 'show_drop_shadow'},
                     2: {'type': 'bool', 'id': 'selected_spread'},
                     3: {'type': 'bool', 'id': 'print_whole_spread'},
                     4: {'type': 'bool', 'id': 'negate_x'},
                     5: {'type': 'bool', 'id': 'negate_y'},
                 }
            }
        ]
    },
    TAG_GRIDRULERSETTINGS: {'name': 'GRIDRULERSETTINGS'},
    TAG_GRIDRULERORIGIN: {'name': 'GRIDRULERORIGIN'},
    TAG_LAYERDETAILS: {
        'name': 'LAYERDETAILS',
        'sec': [
            {'type': 'byte', 'id': 'layer_flags',
                 'bitfield': {
                     0: {'type': 'bool', 'id': 'is_visible'},
                     1: {'type': 'bool', 'id': 'is_locked'},
                     2: {'type': 'bool', 'id': 'is_printable'},
                     3: {'type': 'bool', 'id': 'is_active'},
                 }
             },
            {'type': 'STRING', 'id': 'layer_name'},
        ]
    },
    TAG_GUIDELAYERDETAILS: {'name': 'GUIDELAYERDETAILS'},
    TAG_SPREADSCALING_ACTIVE: {
        'name': 'SPREADSCALING ACTIVE',
        'sec': [
            {'type': 'double', 'id': 'drawing_scale'},
            {'type': 'UNITSREF', 'id': 'drawing_units'},
            {'type': 'double', 'id': 'real_scale'},
            {'type': 'UNITSREF', 'id': 'real_units'},
        ]
    },
    TAG_SPREADSCALING_INACTIVE: {
        'name': 'SPREADSCALING INACTIVE',
        'sec': [
            {'type': 'double', 'id': 'drawing_scale'},
            {'type': 'UNITSREF', 'id': 'drawing_units'},
            {'type': 'double', 'id': 'real_scale'},
            {'type': 'UNITSREF', 'id': 'real_units'},
        ]
    },

    # Colour reference tags
    TAG_DEFINERGBCOLOUR: {'name': 'DEFINERGBCOLOUR'},
    TAG_DEFINECOMPLEXCOLOUR: {
        'name': 'DEFINECOMPLEXCOLOUR',
        'sec': [
            {'type': 'Simple RGBColour', 'id': 'rgbcolor', 'encoding': 'hex'},
            {'type': 'byte', 'id': 'colour_model'},
            {'type': 'byte', 'id': 'colour_type'},
            {'type': 'uint32', 'id': 'entry_index'},
            {'type': 'COLOURREF', 'id': 'parent_colour'},
            {'type': 'fixed24', 'id': 'component1'},
            {'type': 'fixed24', 'id': 'component2'},
            {'type': 'fixed24', 'id': 'component3'},
            {'type': 'fixed24', 'id': 'component4'},
            {'type': 'STRING', 'id': 'colour_name'},
        ]
    },

    # Bitmap reference tags
    TAG_PREVIEWBITMAP_GIF: {'name': 'PREVIEWBITMAP GIF'},
    TAG_PREVIEWBITMAP_JPEG: {'name': 'PREVIEWBITMAP JPEG'},
    TAG_PREVIEWBITMAP_PNG: {'name': 'PREVIEWBITMAP PNG'},

    TAG_DEFINEBITMAP_JPEG: {
        'name': 'DEFINEBITMAP JPEG',
        'sec': [
            {'type': 'STRING', 'id': 'bitmap_name'},
            {'type': 'BITMAP_DATA', 'id': 'bitmap_data'},
        ]
    },
    TAG_DEFINEBITMAP_PNG: {
        'name': 'DEFINEBITMAP PNG',
        'sec': [
            {'type': 'STRING', 'id': 'bitmap_name'},
            {'type': 'BITMAP_DATA', 'id': 'bitmap_data'},
        ]
    },
    TAG_DEFINEBITMAP_JPEG8BPP: {'name': 'DEFINEBITMAP JPEG8BPP'},

    # View tags
    TAG_VIEWPORT: {
        'name': 'VIEWPORT',
        'sec': [
            {'type': 'COORD', 'id': 'bottom_left'},
            {'type': 'COORD', 'id': 'top_right'},
        ]
    },
    TAG_VIEWQUALITY: {'name': 'VIEWQUALITY'},
    TAG_DOCUMENTVIEW: {'name': 'DOCUMENTVIEW'},

    # Document unit tags
    TAG_DEFINE_PREFIXUSERUNIT: {'name': 'DEFINE PREFIXUSERUNIT'},
    TAG_DEFINE_SUFFIXUSERUNIT: {'name': 'DEFINE SUFFIXUSERUNIT'},
    TAG_DEFINE_DEFAULTUNITS: {'name': 'DEFINE DEFAULTUNITS'},

    # Document info tags
    TAG_DOCUMENTCOMMENT: {'name': 'DOCUMENTCOMMENT'},
    TAG_DOCUMENTDATES: {'name': 'DOCUMENTDATES'},
    TAG_DOCUMENTUNDOSIZE: {'name': 'DOCUMENTUNDOSIZE'},
    TAG_DOCUMENTFLAGS: {
        'name': 'DOCUMENTFLAGS',
        'sec': [
            {'type': 'uint32', 'id': 'document_flags',
             'bitfield': {
                    0: {'type': 'bool', 'id': 'multilayer_flag'},
                    1: {'type': 'bool', 'id': 'all_layers_visible_flag'},
                 }
             }
        ]
    },
    TAG_DOCUMENTINFORMATION: {'name': 'DOCUMENTINFORMATION'},

    # Object tags
    TAG_PATH: {'name': 'PATH'},
    TAG_PATH_FILLED: {'name': 'PATH FILLED'},
    TAG_PATH_STROKED: {'name': 'PATH STROKED'},
    TAG_PATH_FILLED_STROKED: {
        'name': 'PATH FILLED STROKED',
        'sec': [
            {'type': 'uint32', 'id': 'number_of_coords'},
            {'type': 'byte', 'id': 'verb', 'number': 'number_of_coords'},
            {'type': 'COORD', 'id': 'coord', 'number': 'number_of_coords'},
        ]
    },
    TAG_GROUP: {'name': 'GROUP', 'sec': None},
    TAG_BLEND: {'name': 'BLEND'},
    TAG_BLENDER: {'name': 'BLENDER'},
    TAG_MOULD_ENVELOPE: {'name': 'MOULD ENVELOPE'},
    TAG_MOULD_PERSPECTIVE: {'name': 'MOULD PERSPECTIVE'},
    TAG_MOULD_GROUP: {'name': 'MOULD GROUP'},
    TAG_MOULD_PATH: {'name': 'MOULD PATH'},
    TAG_PATH_FLAGS: {'name': 'PATH FLAGS'},
    TAG_GUIDELINE: {'name': 'GUIDELINE'},
    TAG_PATH_RELATIVE: {
        'name': 'PATH RELATIVE',
        'sec': [
            {'type': 'Verb and Coord List', 'id': 'path'}
        ]
    },
    TAG_PATH_RELATIVE_FILLED: {
        'name': 'PATH RELATIVE FILLED',
        'sec': [
            {'type': 'Verb and Coord List', 'id': 'path'}
        ]
    },
    TAG_PATH_RELATIVE_STROKED: {
        'name': 'PATH RELATIVE STROKED',
        'sec': [
            {'type': 'Verb and Coord List', 'id': 'path'}
        ]
    },
    TAG_PATH_RELATIVE_FILLED_STROKED: {
        'name': 'PATH RELATIVE FILLED STROKED',
        'sec': [
            {'type': 'Verb and Coord List', 'id': 'path'}
        ]
    },
    TAG_PATHREF_TRANSFORM: {'name': 'PATHREF TRANSFORM'},

    # Attribute tags
    TAG_FLATFILL: {
        'name': 'FLATFILL',
        'sec': [
            {'type': 'COLOURREF', 'id': 'colour'}
        ]
    },
    TAG_LINECOLOUR: {
        'name': 'LINECOLOUR',
        'sec': [
            {'type': 'COLOURREF', 'id': 'colour'}
        ]
    },
    TAG_LINEWIDTH: {
        'name': 'LINEWIDTH',
        'sec': [
            {'type': 'MILLIPOINT', 'id': 'width'}
        ]
    },
    TAG_LINEARFILL: {
        'name': 'LINEARFILL',
        'sec': [
            {'type': 'COORD', 'id': 'start_point'},
            {'type': 'COORD', 'id': 'end_point'},
            {'type': 'COLOURREF', 'id': 'start_colour'},
            {'type': 'COLOURREF', 'id': 'end_colour'},
            {'type': 'double', 'id': 'bias'},
            {'type': 'double', 'id': 'gain'},
            # TODO: support 3 point
        ]
    },
    TAG_CIRCULARFILL: {
        'name': 'CIRCULARFILL',
        'sec': [
            {'type': 'COORD', 'id': 'centre_point'},
            {'type': 'COORD', 'id': 'edge_point'},
            {'type': 'COLOURREF', 'id': 'start_colour'},
            {'type': 'COLOURREF', 'id': 'end_colour'},
            # PROFILE
            {'type': 'double', 'id': 'bias'},
            {'type': 'double', 'id': 'gain'},
        ]
    },
    TAG_ELLIPTICALFILL: {'name': 'ELLIPTICALFILL'},
    TAG_CONICALFILL: {'name': 'CONICALFILL'},
    TAG_BITMAPFILL: {
        'name': 'BITMAPFILL',
        'sec': [
            {'type': 'COORD', 'id': 'bottom_left'},
            {'type': 'COORD', 'id': 'bottom_right'},
            {'type': 'COORD', 'id': 'top_left'},
            {'type': 'BITMAPREF', 'id': 'bitmap'},
            # PROFILE
            {'type': 'double', 'id': 'bias'},
            {'type': 'double', 'id': 'gain'},
        ]
    },
    TAG_CONTONEBITMAPFILL: {'name': 'CONTONEBITMAPFILL'},
    TAG_FRACTALFILL: {'name': 'FRACTALFILL'},
    TAG_FILLEFFECT_FADE: {'name': 'FILLEFFECT FADE'},
    TAG_FILLEFFECT_RAINBOW: {'name': 'FILLEFFECT RAINBOW'},
    TAG_FILLEFFECT_ALTRAINBOW: {'name': 'FILLEFFECT ALTRAINBOW'},
    TAG_FILL_REPEATING: {'name': 'FILL REPEATING'},
    TAG_FILL_NONREPEATING: {'name': 'FILL NONREPEATING'},
    TAG_FILL_REPEATINGINVERTED: {'name': 'FILL REPEATINGINVERTED'},
    TAG_FLATTRANSPARENTFILL: {'name': 'FLATTRANSPARENTFILL'},
    TAG_LINEARTRANSPARENTFILL: {
        'name': 'LINEARTRANSPARENTFILL',
        'sec': [
            {'type': 'COORD', 'id': 'start_point'},
            {'type': 'COORD', 'id': 'end_point'},
            {'type': 'byte', 'id': 'start_transparency'},
            {'type': 'byte', 'id': 'end_transparency'},
            {'type': 'byte', 'id': 'transparency_type'},
            #PROFILE
            {'type': 'double', 'id': 'bias'},
            {'type': 'double', 'id': 'gain'},
            # TODO: support 3 point
        ]
    },
    TAG_CIRCULARTRANSPARENTFILL: {'name': 'CIRCULARTRANSPARENTFILL'},
    TAG_ELLIPTICALTRANSPARENTFILL: {'name': 'ELLIPTICALTRANSPARENTFILL'},
    TAG_CONICALTRANSPARENTFILL: {'name': 'CONICALTRANSPARENTFILL'},
    TAG_BITMAPTRANSPARENTFILL: {'name': 'BITMAPTRANSPARENTFILL'},
    TAG_FRACTALTRANSPARENTFILL: {'name': 'FRACTALTRANSPARENTFILL'},
    TAG_LINETRANSPARENCY: {'name': 'LINETRANSPARENCY'},
    TAG_STARTCAP: {'name': 'STARTCAP'},
    TAG_ENDCAP: {'name': 'ENDCAP'},
    TAG_JOINSTYLE: {'name': 'JOINSTYLE'},
    TAG_MITRELIMIT: {'name': 'MITRELIMIT'},
    TAG_WINDINGRULE: {'name': 'WINDINGRULE'},
    TAG_QUALITY: {'name': 'QUALITY'},
    TAG_TRANSPARENTFILL_REPEATING: {'name': 'TRANSPARENTFILL REPEATING'},
    TAG_TRANSPARENTFILL_NONREPEATING: {'name': 'TRANSPARENTFILL NONREPEATING'},
    TAG_TRANSPARENTFILL_REPEATINGINVERTED: {
        'name': 'TRANSPARENTFILL REPEATINGINVERTED'
    },

    # Arrows and dash patterns
    TAG_DASHSTYLE: {'name': 'DASHSTYLE'},
    TAG_DEFINEDASH: {'name': 'DEFINEDASH'},
    TAG_ARROWHEAD: {'name': 'ARROWHEAD'},
    TAG_ARROWTAIL: {'name': 'ARROWTAIL'},
    TAG_DEFINEARROW: {'name': 'DEFINEARROW'},
    TAG_DEFINEDASH_SCALED: {'name': 'DEFINEDASH SCALED'},

    # User Attributes
    TAG_USERVALUE: {'name': 'USERVALUE'},

    # special colour fills
    TAG_FLATFILL_NONE: {'name': 'FLATFILL NONE'},
    TAG_FLATFILL_BLACK: {'name': 'FLATFILL BLACK'},
    TAG_FLATFILL_WHITE: {'name': 'FLATFILL WHITE'},
    TAG_LINECOLOUR_NONE: {'name': 'LINECOLOUR NONE'},
    TAG_LINECOLOUR_BLACK: {'name': 'LINECOLOUR BLACK'},
    TAG_LINECOLOUR_WHITE: {'name': 'LINECOLOUR WHITE'},

    # Bitmaps
    TAG_NODE_BITMAP: {'name': 'NODE BITMAP'},
    TAG_NODE_CONTONEDBITMAP: {'name': 'NODE CONTONEDBITMAP'},

    # New fill type records
    TAG_DIAMONDFILL: {'name': 'DIAMONDFILL'},
    TAG_DIAMONDTRANSPARENTFILL: {'name': 'DIAMONDTRANSPARENTFILL'},
    TAG_THREECOLFILL: {'name': 'THREECOLFILL'},
    TAG_THREECOLTRANSPARENTFILL: {'name': 'THREECOLTRANSPARENTFILL'},
    TAG_FOURCOLFILL: {'name': 'FOURCOLFILL'},
    TAG_FOURCOLTRANSPARENTFILL: {'name': 'FOURCOLTRANSPARENTFILL'},
    TAG_FILL_REPEATING_EXTRA: {'name': 'FILL REPEATING EXTRA'},
    TAG_TRANSPARENTFILL_REPEATING_EXTRA: {
        'name': 'TRANSPARENTFILL REPEATING EXTRA'
    },

    # Regular shapes

    # Ellipses
    TAG_ELLIPSE_SIMPLE: {'name': 'ELLIPSE SIMPLE'},
    TAG_ELLIPSE_COMPLEX: {'name': 'ELLIPSE COMPLEX'},

    # Rectangles
    TAG_RECTANGLE_SIMPLE: {'name': 'RECTANGLE SIMPLE'},
    TAG_RECTANGLE_SIMPLE_REFORMED: {
        'name': 'RECTANGLE SIMPLE REFORMED', 'deprecated': True
    },
    TAG_RECTANGLE_SIMPLE_STELLATED: {
        'name': 'RECTANGLE SIMPLE STELLATED', 'deprecated': True
    },
    TAG_RECTANGLE_SIMPLE_STELLATED_REFORMED: {
        'name': 'RECTANGLE SIMPLE STELLATED REFORMED', 'deprecated': True
    },
    TAG_RECTANGLE_SIMPLE_ROUNDED: {'name': 'RECTANGLE SIMPLE ROUNDED'},
    TAG_RECTANGLE_SIMPLE_ROUNDED_REFORMED: {
        'name': 'RECTANGLE SIMPLE ROUNDED REFORMED', 'deprecated': True
    },
    TAG_RECTANGLE_SIMPLE_ROUNDED_STELLATED: {
        'name': 'RECTANGLE SIMPLE ROUNDED STELLATED', 'deprecated': True
    },
    TAG_RECTANGLE_SIMPLE_ROUNDED_STELLATED_REFORMED: {
        'name': 'RECTANGLE SIMPLE ROUNDED STELLATED REFORMED',
        'deprecated': True
    },
    TAG_RECTANGLE_COMPLEX: {'name': 'RECTANGLE COMPLEX'},
    TAG_RECTANGLE_COMPLEX_REFORMED: {
        'name': 'RECTANGLE COMPLEX REFORMED', 'deprecated': True
    },
    TAG_RECTANGLE_COMPLEX_STELLATED: {
        'name': 'RECTANGLE COMPLEX STELLATED'
    },
    TAG_RECTANGLE_COMPLEX_STELLATED_REFORMED: {
        'name': 'RECTANGLE COMPLEX STELLATED REFORMED', 'deprecated': True
    },
    TAG_RECTANGLE_COMPLEX_ROUNDED: {'name': 'RECTANGLE COMPLEX ROUNDED'},
    TAG_RECTANGLE_COMPLEX_ROUNDED_REFORMED: {
        'name': 'RECTANGLE COMPLEX ROUNDED REFORMED', 'deprecated': True
    },
    TAG_RECTANGLE_COMPLEX_ROUNDED_STELLATED: {
        'name': 'RECTANGLE COMPLEX ROUNDED STELLATED', 'deprecated': True
    },
    TAG_RECTANGLE_COMPLEX_ROUNDED_STELLATED_REFORMED: {
        'name': 'RECTANGLE COMPLEX ROUNDED STELLATED REFORMED',
        'deprecated': True
    },

    # Polygons
    TAG_POLYGON_COMPLEX: {'name': 'POLYGON COMPLEX'},
    TAG_POLYGON_COMPLEX_REFORMED: {
        'name': 'POLYGON COMPLEX REFORMED', 'deprecated': True
    },
    TAG_POLYGON_COMPLEX_STELLATED: {
        'name': 'POLYGON COMPLEX STELLATED', 'deprecated': True
    },
    TAG_POLYGON_COMPLEX_STELLATED_REFORMED: {
        'name': 'POLYGON COMPLEX STELLATED REFORMED', 'deprecated': True
    },
    TAG_POLYGON_COMPLEX_ROUNDED: {'name': 'POLYGON COMPLEX ROUNDED'},
    TAG_POLYGON_COMPLEX_ROUNDED_REFORMED: {
        'name': 'POLYGON COMPLEX ROUNDED REFORMED'},
    TAG_POLYGON_COMPLEX_ROUNDED_STELLATED: {
        'name': 'POLYGON COMPLEX ROUNDED STELLATED'},
    TAG_POLYGON_COMPLEX_ROUNDED_STELLATED_REFORMED: {
        'name': 'POLYGON COMPLEX ROUNDED STELLATED REFORMED',
        'deprecated': True
    },

    # General regular shapes
    TAG_REGULAR_SHAPE_PHASE_1: {'name': 'REGULAR SHAPE PHASE 1'},
    TAG_REGULAR_SHAPE_PHASE_2: {
        'name': 'REGULAR SHAPE PHASE 2',
        'sec': [
            {'type': 'byte', 'id': 'flags'},
            {'type': 'uint16', 'id': 'number_of_sides'},
            {'type': 'COORD', 'id': 'major_axes'},
            {'type': 'COORD', 'id': 'minor_axes'},

            {'type': 'fixed16', 'id': 'a'},
            {'type': 'fixed16', 'id': 'b'},
            {'type': 'fixed16', 'id': 'c'},
            {'type': 'fixed16', 'id': 'd'},
            {'type': 'int32', 'id': 'e'},
            {'type': 'int32', 'id': 'f'},

            {'type': 'double', 'id': 'stell_radius_to_primary'},
            {'type': 'double', 'id': 'StellOffsetRatio'},
            {'type': 'double', 'id': 'PrimaryCurveToPrimary'},
            {'type': 'double', 'id': 'StellCurveToPrimary'},
            # # {'type': '??', 'id': 'EdgePath1'},
            # # {'type': '??', 'id': 'EdgePath2'},
            # # TODO: ...
        ]
    },

    # Text related records
    # Text definitions
    TAG_FONT_DEF_TRUETYPE: {'name': 'FONT DEF TRUETYPE'},
    TAG_FONT_DEF_ATM: {'name': 'FONT DEF ATM'},

    # vanilla text story objects
    TAG_TEXT_STORY_SIMPLE: {'name': 'TEXT STORY SIMPLE'},
    TAG_TEXT_STORY_COMPLEX: {'name': 'TEXT STORY COMPLEX'},

    # text story objects on a path
    TAG_TEXT_STORY_SIMPLE_START_LEFT: {'name': 'TEXT STORY SIMPLE START LEFT'},
    TAG_TEXT_STORY_SIMPLE_START_RIGHT: {
        'name': 'TEXT STORY SIMPLE START RIGHT'},
    TAG_TEXT_STORY_SIMPLE_END_LEFT: {'name': 'TEXT STORY SIMPLE END LEFT'},
    TAG_TEXT_STORY_SIMPLE_END_RIGHT: {'name': 'TEXT STORY SIMPLE END RIGHT'},
    TAG_TEXT_STORY_COMPLEX_START_LEFT: {
        'name': 'TEXT STORY COMPLEX START LEFT'},
    TAG_TEXT_STORY_COMPLEX_START_RIGHT: {
        'name': 'TEXT STORY COMPLEX START RIGHT'},
    TAG_TEXT_STORY_COMPLEX_END_LEFT: {
        'name': 'TEXT STORY COMPLEX END LEFT', 'deprecated': True
    },
    TAG_TEXT_STORY_COMPLEX_END_RIGHT: {'name': 'TEXT STORY COMPLEX END RIGHT'},

    # Text story information records
    TAG_TEXT_STORY_WORD_WRAP_INFO: {'name': 'TEXT STORY WORD WRAP INFO'},
    TAG_TEXT_STORY_INDENT_INFO: {'name': 'TEXT STORY INDENT INFO'},

    # other text story related objects
    TAG_TEXT_LINE: {'name': 'TEXT LINE'},
    TAG_TEXT_STRING: {'name': 'TEXT STRING'},
    TAG_TEXT_CHAR: {'name': 'TEXT CHAR'},
    TAG_TEXT_EOL: {'name': 'TEXT EOL'},
    TAG_TEXT_KERN: {'name': 'TEXT KERN'},
    TAG_TEXT_CARET: {'name': 'TEXT CARET'},
    TAG_TEXT_LINE_INFO: {'name': 'TEXT LINE INFO'},

    # Text attributes
    TAG_TEXT_LINESPACE_RATIO: {'name': 'TEXT LINESPACE RATIO'},
    TAG_TEXT_LINESPACE_ABSOLUTE: {'name': 'TEXT LINESPACE ABSOLUTE'},
    TAG_TEXT_JUSTIFICATION_LEFT: {'name': 'TEXT JUSTIFICATION LEFT'},
    TAG_TEXT_JUSTIFICATION_CENTRE: {'name': 'TEXT JUSTIFICATION CENTRE'},
    TAG_TEXT_JUSTIFICATION_RIGHT: {'name': 'TEXT JUSTIFICATION RIGHT'},
    TAG_TEXT_JUSTIFICATION_FULL: {'name': 'TEXT JUSTIFICATION FULL'},
    TAG_TEXT_FONT_SIZE: {'name': 'TEXT FONT SIZE'},
    TAG_TEXT_FONT_TYPEFACE: {'name': 'TEXT FONT TYPEFACE'},
    TAG_TEXT_BOLD_ON: {'name': 'TEXT BOLD ON'},
    TAG_TEXT_BOLD_OFF: {'name': 'TEXT BOLD OFF'},
    TAG_TEXT_ITALIC_ON: {'name': 'TEXT ITALIC ON'},
    TAG_TEXT_ITALIC_OFF: {'name': 'TEXT ITALIC OFF'},
    TAG_TEXT_UNDERLINE_ON: {'name': 'TEXT UNDERLINE ON'},
    TAG_TEXT_UNDERLINE_OFF: {'name': 'TEXT UNDERLINE OFF'},
    TAG_TEXT_SCRIPT_ON: {'name': 'TEXT SCRIPT ON'},
    TAG_TEXT_SCRIPT_OFF: {'name': 'TEXT SCRIPT OFF'},
    TAG_TEXT_SUPERSCRIPT_ON: {'name': 'TEXT SUPERSCRIPT ON'},
    TAG_TEXT_SUBSCRIPT_ON: {'name': 'TEXT SUBSCRIPT ON'},
    TAG_TEXT_TRACKING: {'name': 'TEXT TRACKING'},
    TAG_TEXT_ASPECT_RATIO: {'name': 'TEXT ASPECT RATIO'},
    TAG_TEXT_BASELINE: {'name': 'TEXT BASELINE'},

    # Imagesetting attributes
    TAG_OVERPRINTLINEON: {'name': 'OVERPRINTLINEON'},
    TAG_OVERPRINTLINEOFF: {'name': 'OVERPRINTLINEOFF'},
    TAG_OVERPRINTFILLON: {'name': 'OVERPRINTFILLON'},
    TAG_OVERPRINTFILLOFF: {'name': 'OVERPRINTFILLOFF'},
    TAG_PRINTONALLPLATESON: {'name': 'PRINTONALLPLATESON'},
    TAG_PRINTONALLPLATESOFF: {'name': 'PRINTONALLPLATESOFF'},

    # Document Print/Image setting options
    TAG_PRINTERSETTINGS: {'name': 'PRINTERSETTINGS'},
    TAG_IMAGESETTING: {'name': 'IMAGESETTING'},
    TAG_COLOURPLATE: {'name': 'COLOURPLATE'},

    # Registration mark records
    TAG_PRINTMARKDEFAULT: {'name': 'PRINTMARKDEFAULT'},

    # Stroking records
    TAG_VARIABLEWIDTHFUNC: {'name': 'VARIABLEWIDTHFUNC'},
    TAG_VARIABLEWIDTHTABLE: {'name': 'VARIABLEWIDTHTABLE'},
    TAG_STROKETYPE: {'name': 'STROKETYPE'},
    TAG_STROKEDEFINITION: {'name': 'STROKEDEFINITION'},
    TAG_STROKEAIRBRUSH: {'name': 'STROKEAIRBRUSH'},

    # Fractal Noise records
    TAG_NOISEFILL: {'name': 'NOISEFILL'},
    TAG_NOISETRANSPARENTFILL: {'name': 'NOISETRANSPARENTFILL'},

    # Mould bounds record
    TAG_MOULD_BOUNDS: {'name': 'MOULD BOUNDS'},

    # Bitmap export hint record
    TAG_EXPORT_HINT: {'name': 'EXPORT HINT'},

    # Web Address tags
    TAG_WEBADDRESS: {'name': 'WEBADDRESS'},
    TAG_WEBADDRESS_BOUNDINGBOX: {'name': 'WEBADDRESS BOUNDINGBOX'},

    # Frame layer tags
    TAG_LAYER_FRAMEPROPS: {'name': 'LAYER FRAMEPROPS'},
    TAG_SPREAD_ANIMPROPS: {'name': 'SPREAD ANIMPROPS'},

    # Wizard properties tags
    TAG_WIZOP: {'name': 'WIZOP'},
    TAG_WIZOP_STYLE: {'name': 'WIZOP STYLE'},
    TAG_WIZOP_STYLEREF: {'name': 'WIZOP STYLEREF'},

    # Shadow tags
    TAG_SHADOWCONTROLLER: {'name': 'SHADOWCONTROLLER'},
    TAG_SHADOW: {'name': 'SHADOW'},

    # Bevel tags
    TAG_BEVEL: {'name': 'BEVEL'},
    TAG_BEVATTR_INDENT: {'name': 'BEVATTR INDENT', 'deprecated': True},
    TAG_BEVATTR_LIGHTANGLE: {'name': 'BEVATTR LIGHTANGLE', 'deprecated': True},
    TAG_BEVATTR_CONTRAST: {'name': 'BEVATTR CONTRAST', 'deprecated': True},
    TAG_BEVATTR_TYPE: {'name': 'BEVATTR TYPE', 'deprecated': True},
    TAG_BEVELINK: {'name': 'BEVELINK'},

    # Blend on a curve tags
    TAG_BLENDER_CURVEPROP: {'name': 'BLENDER CURVEPROP'},
    TAG_BLEND_PATH: {'name': 'BLEND PATH'},
    TAG_BLENDER_CURVEANGLES: {'name': 'BLENDER CURVEANGLES'},

    # Contouring tags
    TAG_CONTOURCONTROLLER: {'name': 'CONTOURCONTROLLER'},
    TAG_CONTOUR: {'name': 'CONTOUR'},

    # Set tags
    TAG_SETSENTINEL: {'name': 'SETSENTINEL'},
    TAG_SETPROPERTY: {'name': 'SETPROPERTY'},

    # More Blend on a curve tags
    TAG_BLENDPROFILES: {'name': 'BLENDPROFILES'},
    TAG_BLENDERADDITIONAL: {'name': 'BLENDERADDITIONAL'},
    TAG_NODEBLENDPATH_FILLED: {'name': 'NODEBLENDPATH FILLED'},

    # Multi stage fill tags
    TAG_LINEARFILLMULTISTAGE: {
        'name': 'LINEARFILLMULTISTAGE',
        'sec': [
            {'type': 'COORD', 'id': 'start_point'},
            {'type': 'COORD', 'id': 'end_point'},
            {'type': 'COLOURREF', 'id': 'start_colour'},
            {'type': 'COLOURREF', 'id': 'end_colour'},
            {'type': 'uint32', 'id': 'num_cols'},
            {'type': 'StopColour', 'id': 'stop_colors', 'number': 'num_cols'}
            # {'type': 'double', 'id': 'position'},
            # {'type': 'COLOURREF', 'id': 'colour'},
        ]
    },
    TAG_CIRCULARFILLMULTISTAGE: {
        'name': 'CIRCULARFILLMULTISTAGE',
        'sec': [
            {'type': 'COORD', 'id': 'centre_point'},
            {'type': 'COORD', 'id': 'edge_point'},
            {'type': 'COLOURREF', 'id': 'start_colour'},
            {'type': 'COLOURREF', 'id': 'end_colour'},
            {'type': 'uint32', 'id': 'num_cols'},
            {'type': 'StopColour', 'id': 'stop_colors', 'number': 'num_cols'}
        ]
     },
    TAG_ELLIPTICALFILLMULTISTAGE: {'name': 'ELLIPTICALFILLMULTISTAGE'},
    TAG_CONICALFILLMULTISTAGE: {'name': 'CONICALFILLMULTISTAGE'},

    # Brush attribute tags
    TAG_BRUSHATTR: {'name': 'BRUSHATTR'},
    TAG_BRUSHDEFINITION: {'name': 'BRUSHDEFINITION'},
    TAG_BRUSHDATA: {'name': 'BRUSHDATA'},
    TAG_MOREBRUSHDATA: {'name': 'MOREBRUSHDATA'},
    TAG_MOREBRUSHATTR: {'name': 'MOREBRUSHATTR'},

    # ClipView tags
    TAG_CLIPVIEWCONTROLLER: {'name': 'CLIPVIEWCONTROLLER'},
    TAG_CLIPVIEW: {'name': 'CLIPVIEW'},

    # Feathering tags
    TAG_FEATHER: {'name': 'FEATHER'},

    # Bar properties tag
    TAG_BARPROPERTY: {'name': 'BARPROPERTY'},

    # Other multi stage fill tags
    TAG_SQUAREFILLMULTISTAGE: {'name': 'SQUAREFILLMULTISTAGE'},

    # More brush tags
    TAG_EVENMOREBRUSHDATA: {'name': 'EVENMOREBRUSHDATA'},
    TAG_EVENMOREBRUSHATTR: {'name': 'EVENMOREBRUSHATTR'},
    TAG_TIMESTAMPBRUSHDATA: {'name': 'TIMESTAMPBRUSHDATA'},
    TAG_BRUSHPRESSUREINFO: {'name': 'BRUSHPRESSUREINFO'},
    TAG_BRUSHPRESSUREDATA: {'name': 'BRUSHPRESSUREDATA'},
    TAG_BRUSHATTRPRESSUREINFO: {'name': 'BRUSHATTRPRESSUREINFO'},
    TAG_BRUSHCOLOURDATA: {'name': 'BRUSHCOLOURDATA'},
    TAG_BRUSHPRESSURESAMPLEDATA: {'name': 'BRUSHPRESSURESAMPLEDATA'},
    TAG_BRUSHTIMESAMPLEDATA: {'name': 'BRUSHTIMESAMPLEDATA'},
    TAG_BRUSHATTRFILLFLAGS: {'name': 'BRUSHATTRFILLFLAGS'},
    TAG_BRUSHTRANSPINFO: {'name': 'BRUSHTRANSPINFO'},
    TAG_BRUSHATTRTRANSPINFO: {'name': 'BRUSHATTRTRANSPINFO'},

    # Nudge size record
    TAG_DOCUMENTNUDGE: {
        'name': 'DOCUMENTNUDGE',
        'sec': [
            {'type': 'MILLIPOINT', 'id': 'size'}
        ]
    },

    # Bitmap properties record
    TAG_BITMAP_PROPERTIES: {'name': 'BITMAP PROPERTIES'},

    # Bitmap smoothing record
    TAG_DOCUMENTBITMAPSMOOTHING: {'name': 'DOCUMENTBITMAPSMOOTHING'},

    # XPE bitmap processing record
    TAG_XPE_BITMAP_PROPERTIES: {'name': 'XPE BITMAP PROPERTIES'},

    # XPE Bitmap file format placeholder record
    TAG_DEFINEBITMAP_XPE: {'name': 'DEFINEBITMAP XPE'},

    # Current attributes records
    TAG_CURRENTATTRIBUTES: {
        'name': 'CURRENTATTRIBUTES',
        'sec': [
            {'type': 'byte', 'id': 'group'}
        ]
    },
    TAG_CURRENTATTRIBUTEBOUNDS: {'name': 'CURRENTATTRIBUTEBOUNDS'},

    # 3-point linear fill records
    TAG_LINEARFILL3POINT: {'name': 'LINEARFILL3POINT'},
    TAG_LINEARFILLMULTISTAGE3POINT: {'name': 'LINEARFILLMULTISTAGE3POINT'},
    TAG_LINEARTRANSPARENTFILL3POINT: {'name': 'LINEARTRANSPARENTFILL3POINT'},

    # Duplication distance record
    TAG_DUPLICATIONOFFSET: {'name': 'DUPLICATIONOFFSET'},

    # Bitmap effect tags
    TAG_LIVE_EFFECT: {'name': 'LIVE EFFECT'},
    TAG_LOCKED_EFFECT: {'name': 'LOCKED EFFECT'},
    TAG_FEATHER_EFFECT: {'name': 'FEATHER EFFECT'},

    # Miscellaneous records
    TAG_COMPOUNDRENDER: {'name': 'COMPOUNDRENDER'},
    TAG_OBJECTBOUNDS: {'name': 'OBJECTBOUNDS'},
    TAG_SPREAD_PHASE2: {'name': 'SPREAD PHASE2'},
    TAG_CURRENTATTRIBUTES_PHASE2: {'name': 'CURRENTATTRIBUTES PHASE2'},
    TAG_SPREAD_FLASHPROPS: {'name': 'SPREAD FLASHPROPS'},
    TAG_PRINTERSETTINGS_PHASE2: {'name': 'PRINTERSETTINGS PHASE2'},
    TAG_DOCUMENTINFORMATION: {'name': 'DOCUMENTINFORMATION'},
    TAG_CLIPVIEW_PATH: {'name': 'CLIPVIEW PATH'},
    TAG_DEFINEBITMAP_PNG_REAL: {
        'name': 'DEFINEBITMAP PNG REAL',
        'sec': [
            {'type': 'STRING', 'id': 'bitmap_name'},
            {'type': 'BITMAP_DATA', 'id': 'bitmap_data'},
        ]
    },
    TAG_TEXT_STRING_POS: {'name': 'TEXT STRING POS'},
    TAG_SPREAD_FLASHPROPS2: {'name': 'SPREAD FLASHPROPS2'},
    TAG_TEXT_LINESPACE_LEADING: {'name': 'TEXT LINESPACE LEADING'},

    # New text records
    TAG_TEXT_TAB: {'name': 'TEXT TAB'},
    TAG_TEXT_LEFT_INDENT: {'name': 'TEXT LEFT INDENT'},
    TAG_TEXT_FIRST_INDENT: {'name': 'TEXT FIRST INDENT'},
    TAG_TEXT_RIGHT_INDENT: {'name': 'TEXT RIGHT INDENT'},
    TAG_TEXT_RULER: {'name': 'TEXT RULER'},
    TAG_TEXT_STORY_HEIGHT_INFO: {'name': 'TEXT STORY HEIGHT INFO'},
    TAG_TEXT_STORY_LINK_INFO: {'name': 'TEXT STORY LINK INFO'},
    TAG_TEXT_STORY_TRANSLATION_INFO: {'name': 'TEXT STORY TRANSLATION INFO'},
    TAG_TEXT_SPACE_BEFORE: {'name': 'TEXT SPACE BEFORE'},
    TAG_TEXT_SPACE_AFTER: {'name': 'TEXT SPACE AFTER'},
    TAG_TEXT_SPECIAL_HYPHEN: {'name': 'TEXT SPECIAL HYPHEN'},
    TAG_TEXT_SOFT_RETURN: {'name': 'TEXT SOFT RETURN'},
    TAG_TEXT_EXTRA_FONT_INFO: {'name': 'TEXT EXTRA FONT INFO'},
    TAG_TEXT_EXTRA_TT_FONT_DEF: {'name': 'TEXT EXTRA TT FONT DEF'},
    TAG_TEXT_EXTRA_ATM_FONT_DEF: {'name': 'TEXT EXTRA ATM FONT DEF'},
}
