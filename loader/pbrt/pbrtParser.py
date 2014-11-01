# Generated from java-escape by ANTLR 4.4
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .pbrtListener import pbrtListener
else:
    from pbrtListener import pbrtListener
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\61")
        buf.write("\u011f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\6\4E\n\4\r\4\16\4F\3")
        buf.write("\4\3\4\3\4\6\4L\n\4\r\4\16\4M\3\4\5\4Q\n\4\3\5\3\5\3\5")
        buf.write("\7\5V\n\5\f\5\16\5Y\13\5\3\6\3\6\3\6\7\6^\n\6\f\6\16\6")
        buf.write("a\13\6\3\7\3\7\3\7\7\7f\n\7\f\7\16\7i\13\7\3\b\3\b\3\b")
        buf.write("\7\bn\n\b\f\b\16\bq\13\b\3\t\3\t\3\t\7\tv\n\t\f\t\16\t")
        buf.write("y\13\t\3\n\3\n\3\n\7\n~\n\n\f\n\16\n\u0081\13\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\6\r\u0096\n\r\r\r\16\r\u0097\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u00a2\n\16\f")
        buf.write("\16\16\16\u00a5\13\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\7\17\u00b1\n\17\f\17\16\17\u00b4\13")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\7\20\u00c1\n\20\f\20\16\20\u00c4\13\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\7\21\u00cb\n\21\f\21\16\21\u00ce\13\21")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\23\7\23\u00d7\n\23\f")
        buf.write("\23\16\23\u00da\13\23\3\24\3\24\3\24\7\24\u00df\n\24\f")
        buf.write("\24\16\24\u00e2\13\24\3\25\3\25\3\26\3\26\3\26\6\26\u00e9")
        buf.write("\n\26\r\26\16\26\u00ea\3\27\3\27\3\27\3\27\3\27\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\31\3\31\7\31\u00f9\n\31\f\31\16\31")
        buf.write("\u00fc\13\31\3\32\3\32\7\32\u0100\n\32\f\32\16\32\u0103")
        buf.write("\13\32\3\33\3\33\3\34\3\34\7\34\u0109\n\34\f\34\16\34")
        buf.write("\u010c\13\34\3\35\3\35\3\35\6\35\u0111\n\35\r\35\16\35")
        buf.write("\u0112\3\35\3\35\3\35\6\35\u0118\n\35\r\35\16\35\u0119")
        buf.write("\3\35\5\35\u011d\n\35\3\35\2\2\36\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668\2\2\u0138\2:")
        buf.write("\3\2\2\2\4>\3\2\2\2\6@\3\2\2\2\bR\3\2\2\2\nZ\3\2\2\2\f")
        buf.write("b\3\2\2\2\16j\3\2\2\2\20r\3\2\2\2\22z\3\2\2\2\24\u0082")
        buf.write("\3\2\2\2\26\u0087\3\2\2\2\30\u0095\3\2\2\2\32\u0099\3")
        buf.write("\2\2\2\34\u00a8\3\2\2\2\36\u00b7\3\2\2\2 \u00c7\3\2\2")
        buf.write("\2\"\u00d1\3\2\2\2$\u00d3\3\2\2\2&\u00db\3\2\2\2(\u00e3")
        buf.write("\3\2\2\2*\u00e5\3\2\2\2,\u00ec\3\2\2\2.\u00f1\3\2\2\2")
        buf.write("\60\u00f6\3\2\2\2\62\u00fd\3\2\2\2\64\u0104\3\2\2\2\66")
        buf.write("\u0106\3\2\2\28\u011c\3\2\2\2:;\7\4\2\2;<\7\4\2\2<=\7")
        buf.write("\4\2\2=\3\3\2\2\2>?\7\3\2\2?\5\3\2\2\2@P\5\4\3\2AQ\7\3")
        buf.write("\2\2BD\7\60\2\2CE\7\4\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2")
        buf.write("\2FG\3\2\2\2GH\3\2\2\2HQ\7\61\2\2IK\7\60\2\2JL\7\3\2\2")
        buf.write("KJ\3\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NO\3\2\2\2OQ\7")
        buf.write("\61\2\2PA\3\2\2\2PB\3\2\2\2PI\3\2\2\2Q\7\3\2\2\2RS\7\22")
        buf.write("\2\2SW\7\3\2\2TV\5\6\4\2UT\3\2\2\2VY\3\2\2\2WU\3\2\2\2")
        buf.write("WX\3\2\2\2X\t\3\2\2\2YW\3\2\2\2Z[\7\36\2\2[_\7\3\2\2\\")
        buf.write("^\5\6\4\2]\\\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`\13")
        buf.write("\3\2\2\2a_\3\2\2\2bc\7!\2\2cg\7\3\2\2df\5\6\4\2ed\3\2")
        buf.write("\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2h\r\3\2\2\2ig\3\2\2")
        buf.write("\2jk\7\35\2\2ko\7\3\2\2ln\5\6\4\2ml\3\2\2\2nq\3\2\2\2")
        buf.write("om\3\2\2\2op\3\2\2\2p\17\3\2\2\2qo\3\2\2\2rs\7%\2\2sw")
        buf.write("\7\3\2\2tv\5\6\4\2ut\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx\3\2")
        buf.write("\2\2x\21\3\2\2\2yw\3\2\2\2z{\7\r\2\2{\177\7\3\2\2|~\5")
        buf.write("\6\4\2}|\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080")
        buf.write("\3\2\2\2\u0080\23\3\2\2\2\u0081\177\3\2\2\2\u0082\u0083")
        buf.write("\7\26\2\2\u0083\u0084\5\2\2\2\u0084\u0085\5\2\2\2\u0085")
        buf.write("\u0086\5\2\2\2\u0086\25\3\2\2\2\u0087\u0088\5\30\r\2\u0088")
        buf.write("\u0089\7\2\2\3\u0089\27\3\2\2\2\u008a\u0096\5,\27\2\u008b")
        buf.write("\u0096\58\35\2\u008c\u0096\5.\30\2\u008d\u0096\5\b\5\2")
        buf.write("\u008e\u0096\5\n\6\2\u008f\u0096\5\f\7\2\u0090\u0096\5")
        buf.write("\16\b\2\u0091\u0096\5\20\t\2\u0092\u0096\5\22\n\2\u0093")
        buf.write("\u0096\5\24\13\2\u0094\u0096\5\32\16\2\u0095\u008a\3\2")
        buf.write("\2\2\u0095\u008b\3\2\2\2\u0095\u008c\3\2\2\2\u0095\u008d")
        buf.write("\3\2\2\2\u0095\u008e\3\2\2\2\u0095\u008f\3\2\2\2\u0095")
        buf.write("\u0090\3\2\2\2\u0095\u0091\3\2\2\2\u0095\u0092\3\2\2\2")
        buf.write("\u0095\u0093\3\2\2\2\u0095\u0094\3\2\2\2\u0096\u0097\3")
        buf.write("\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\31")
        buf.write("\3\2\2\2\u0099\u00a3\7.\2\2\u009a\u00a2\5\66\34\2\u009b")
        buf.write("\u00a2\5$\23\2\u009c\u00a2\5\62\32\2\u009d\u00a2\5&\24")
        buf.write("\2\u009e\u00a2\5\"\22\2\u009f\u00a2\5\36\20\2\u00a0\u00a2")
        buf.write("\5\34\17\2\u00a1\u009a\3\2\2\2\u00a1\u009b\3\2\2\2\u00a1")
        buf.write("\u009c\3\2\2\2\u00a1\u009d\3\2\2\2\u00a1\u009e\3\2\2\2")
        buf.write("\u00a1\u009f\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\u00a5\3")
        buf.write("\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a6")
        buf.write("\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a7\7/\2\2\u00a7")
        buf.write("\33\3\2\2\2\u00a8\u00b2\7\32\2\2\u00a9\u00b1\5\64\33\2")
        buf.write("\u00aa\u00b1\5&\24\2\u00ab\u00b1\5,\27\2\u00ac\u00b1\5")
        buf.write(".\30\2\u00ad\u00b1\5(\25\2\u00ae\u00b1\5$\23\2\u00af\u00b1")
        buf.write("\5\36\20\2\u00b0\u00a9\3\2\2\2\u00b0\u00aa\3\2\2\2\u00b0")
        buf.write("\u00ab\3\2\2\2\u00b0\u00ac\3\2\2\2\u00b0\u00ad\3\2\2\2")
        buf.write("\u00b0\u00ae\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1\u00b4\3")
        buf.write("\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b5")
        buf.write("\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00b6\7\33\2\2\u00b6")
        buf.write("\35\3\2\2\2\u00b7\u00c2\7\13\2\2\u00b8\u00c1\5\64\33\2")
        buf.write("\u00b9\u00c1\5&\24\2\u00ba\u00c1\5\60\31\2\u00bb\u00c1")
        buf.write("\5*\26\2\u00bc\u00c1\5(\25\2\u00bd\u00c1\5,\27\2\u00be")
        buf.write("\u00c1\5.\30\2\u00bf\u00c1\5$\23\2\u00c0\u00b8\3\2\2\2")
        buf.write("\u00c0\u00b9\3\2\2\2\u00c0\u00ba\3\2\2\2\u00c0\u00bb\3")
        buf.write("\2\2\2\u00c0\u00bc\3\2\2\2\u00c0\u00bd\3\2\2\2\u00c0\u00be")
        buf.write("\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2")
        buf.write("\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c5\3\2\2\2")
        buf.write("\u00c4\u00c2\3\2\2\2\u00c5\u00c6\7\f\2\2\u00c6\37\3\2")
        buf.write("\2\2\u00c7\u00cc\7\'\2\2\u00c8\u00cb\5\"\22\2\u00c9\u00cb")
        buf.write("\5$\23\2\u00ca\u00c8\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb")
        buf.write("\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2")
        buf.write("\u00cd\u00cf\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d0\7")
        buf.write("(\2\2\u00d0!\3\2\2\2\u00d1\u00d2\7*\2\2\u00d2#\3\2\2\2")
        buf.write("\u00d3\u00d4\7#\2\2\u00d4\u00d8\7\3\2\2\u00d5\u00d7\5")
        buf.write("\6\4\2\u00d6\u00d5\3\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d6")
        buf.write("\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9%\3\2\2\2\u00da\u00d8")
        buf.write("\3\2\2\2\u00db\u00dc\7\30\2\2\u00dc\u00e0\7\3\2\2\u00dd")
        buf.write("\u00df\5\6\4\2\u00de\u00dd\3\2\2\2\u00df\u00e2\3\2\2\2")
        buf.write("\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\'\3\2\2")
        buf.write("\2\u00e2\u00e0\3\2\2\2\u00e3\u00e4\7 \2\2\u00e4)\3\2\2")
        buf.write("\2\u00e5\u00e6\7\25\2\2\u00e6\u00e8\7\3\2\2\u00e7\u00e9")
        buf.write("\5\6\4\2\u00e8\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea")
        buf.write("\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb+\3\2\2\2\u00ec")
        buf.write("\u00ed\7+\2\2\u00ed\u00ee\7\4\2\2\u00ee\u00ef\7\4\2\2")
        buf.write("\u00ef\u00f0\7\4\2\2\u00f0-\3\2\2\2\u00f1\u00f2\7\"\2")
        buf.write("\2\u00f2\u00f3\7\4\2\2\u00f3\u00f4\7\4\2\2\u00f4\u00f5")
        buf.write("\7\4\2\2\u00f5/\3\2\2\2\u00f6\u00fa\7\n\2\2\u00f7\u00f9")
        buf.write("\5\6\4\2\u00f8\u00f7\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa")
        buf.write("\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\61\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fd\u0101\7&\2\2\u00fe\u0100\5\6\4\2")
        buf.write("\u00ff\u00fe\3\2\2\2\u0100\u0103\3\2\2\2\u0101\u00ff\3")
        buf.write("\2\2\2\u0101\u0102\3\2\2\2\u0102\63\3\2\2\2\u0103\u0101")
        buf.write("\3\2\2\2\u0104\u0105\7\24\2\2\u0105\65\3\2\2\2\u0106\u010a")
        buf.write("\7\34\2\2\u0107\u0109\5\6\4\2\u0108\u0107\3\2\2\2\u0109")
        buf.write("\u010c\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2")
        buf.write("\u010b\67\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u010e\7\16")
        buf.write("\2\2\u010e\u0110\7\60\2\2\u010f\u0111\7\4\2\2\u0110\u010f")
        buf.write("\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0110\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u011d\7\61\2")
        buf.write("\2\u0115\u0117\7\60\2\2\u0116\u0118\7\3\2\2\u0117\u0116")
        buf.write("\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u0117\3\2\2\2\u0119")
        buf.write("\u011a\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011d\7\61\2")
        buf.write("\2\u011c\u010d\3\2\2\2\u011c\u0115\3\2\2\2\u011d9\3\2")
        buf.write("\2\2\36FMPW_gow\177\u0095\u0097\u00a1\u00a3\u00b0\u00b2")
        buf.write("\u00c0\u00c2\u00ca\u00cc\u00d8\u00e0\u00ea\u00fa\u0101")
        buf.write("\u010a\u0112\u0119\u011c")
        return buf.getvalue()
		

class pbrtParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    STRING=1
    NUMBER=2
    WS=3
    LINE_COMMENT=4
    ACCELERATOR=5
    ACTIVETRANSFORM=6
    ALL=7
    AREALIGHTSOURCE=8
    ATTRIBUTEBEGIN=9
    ATTRIBUTEEND=10
    CAMERA=11
    CONCATTRANSFORM=12
    COORDINATESYSTEM=13
    COORDSYSTRANSFORM=14
    ENDTIME=15
    FILM=16
    IDENTITY=17
    INCLUDE=18
    LIGHTSOURCE=19
    LOOKAT=20
    MAKENAMEDMATERIAL=21
    MATERIAL=22
    NAMEDMATERIAL=23
    OBJECTBEGIN=24
    OBJECTEND=25
    OBJECTINSTANCE=26
    PIXELFILTER=27
    RENDERER=28
    REVERSEORIENTATION=29
    ROTATE=30
    SAMPLER=31
    SCALE=32
    SHAPE=33
    STARTTIME=34
    SURFACEINTEGRATOR=35
    TEXTURE=36
    TRANSFORMBEGIN=37
    TRANSFORMEND=38
    TRANSFORMTIMES=39
    TRANSFORM=40
    TRANSLATE=41
    VOLUME=42
    VOLUMEINTEGRATOR=43
    WORLDBEGIN=44
    WORLDEND=45
    PARAMSET_ITEM_LIST_START=46
    PARAMSET_ITEM_LIST_END=47

    tokenNames = [ "<INVALID>", "STRING", "NUMBER", "WS", "LINE_COMMENT", 
                   "'Accelerator'", "'ActiveTransform'", "'All'", "'AreaLightSource'", 
                   "'AttributeBegin'", "'AttributeEnd'", "'Camera'", "'ConcatTransform'", 
                   "'CoordinateSystem'", "'CoordSysTransform'", "'EndTime'", 
                   "'Film'", "'Identity'", "'Include'", "'LightSource'", 
                   "'LookAt'", "'MakeNamedMaterial'", "'Material'", "'NamedMaterial'", 
                   "'ObjectBegin'", "'ObjectEnd'", "'ObjectInstance'", "'PixelFilter'", 
                   "'Renderer'", "'ReverseOrientation'", "'Rotate'", "'Sampler'", 
                   "'Scale'", "'Shape'", "'StartTime'", "'SurfaceIntegrator'", 
                   "'Texture'", "'TransformBegin'", "'TransformEnd'", "'TransformTimes'", 
                   "'Transform'", "'Translate'", "'Volume'", "'VolumeIntegrator'", 
                   "'WorldBegin'", "'WorldEnd'", "'['", "']'" ]

    RULE_vector3 = 0
    RULE_paramSetLeft = 1
    RULE_paramSet = 2
    RULE_film = 3
    RULE_renderer = 4
    RULE_sampler = 5
    RULE_pixelFilter = 6
    RULE_surfaceIntegrator = 7
    RULE_camera = 8
    RULE_lookAt = 9
    RULE_program = 10
    RULE_body = 11
    RULE_worldBlock = 12
    RULE_objectBlock = 13
    RULE_attributeBlock = 14
    RULE_transformBlock = 15
    RULE_transform = 16
    RULE_shape = 17
    RULE_material = 18
    RULE_rotate = 19
    RULE_lightSource = 20
    RULE_translate = 21
    RULE_scale = 22
    RULE_areaLightSource = 23
    RULE_texture = 24
    RULE_include = 25
    RULE_objectInstance = 26
    RULE_concattransform = 27

    ruleNames =  [ "vector3", "paramSetLeft", "paramSet", "film", "renderer", 
                   "sampler", "pixelFilter", "surfaceIntegrator", "camera", 
                   "lookAt", "program", "body", "worldBlock", "objectBlock", 
                   "attributeBlock", "transformBlock", "transform", "shape", 
                   "material", "rotate", "lightSource", "translate", "scale", 
                   "areaLightSource", "texture", "include", "objectInstance", 
                   "concattransform" ]

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.4")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Vector3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(pbrtParser.NUMBER)
            else:
                return self.getToken(pbrtParser.NUMBER, i)

        def getRuleIndex(self):
            return pbrtParser.RULE_vector3

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterVector3(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitVector3(self)




    def vector3(self):

        localctx = pbrtParser.Vector3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_vector3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(self.NUMBER)
            self.state = 57
            self.match(self.NUMBER)
            self.state = 58
            self.match(self.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParamSetLeftContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(pbrtParser.STRING, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_paramSetLeft

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterParamSetLeft(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitParamSetLeft(self)




    def paramSetLeft(self):

        localctx = pbrtParser.ParamSetLeftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_paramSetLeft)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(self.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParamSetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(pbrtParser.STRING)
            else:
                return self.getToken(pbrtParser.STRING, i)

        def paramSetLeft(self):
            return self.getTypedRuleContext(pbrtParser.ParamSetLeftContext,0)


        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(pbrtParser.NUMBER)
            else:
                return self.getToken(pbrtParser.NUMBER, i)

        def getRuleIndex(self):
            return pbrtParser.RULE_paramSet

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterParamSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitParamSet(self)




    def paramSet(self):

        localctx = pbrtParser.ParamSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_paramSet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62 
            self.paramSetLeft()
            self.state = 78
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 63
                self.match(self.STRING)
                pass

            elif la_ == 2:
                self.state = 64
                self.match(self.PARAMSET_ITEM_LIST_START)
                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 65
                    self.match(self.NUMBER)
                    self.state = 68 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==pbrtParser.NUMBER):
                        break

                self.state = 70
                self.match(self.PARAMSET_ITEM_LIST_END)
                pass

            elif la_ == 3:
                self.state = 71
                self.match(self.PARAMSET_ITEM_LIST_START)
                self.state = 73 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 72
                    self.match(self.STRING)
                    self.state = 75 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==pbrtParser.STRING):
                        break

                self.state = 77
                self.match(self.PARAMSET_ITEM_LIST_END)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FilmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramSet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ParamSetContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ParamSetContext,i)


        def FILM(self):
            return self.getToken(pbrtParser.FILM, 0)

        def STRING(self):
            return self.getToken(pbrtParser.STRING, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_film

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterFilm(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitFilm(self)




    def film(self):

        localctx = pbrtParser.FilmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_film)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(self.FILM)
            self.state = 81
            self.match(self.STRING)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pbrtParser.STRING:
                self.state = 82 
                self.paramSet()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RendererContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramSet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ParamSetContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ParamSetContext,i)


        def RENDERER(self):
            return self.getToken(pbrtParser.RENDERER, 0)

        def STRING(self):
            return self.getToken(pbrtParser.STRING, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_renderer

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterRenderer(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitRenderer(self)




    def renderer(self):

        localctx = pbrtParser.RendererContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_renderer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(self.RENDERER)
            self.state = 89
            self.match(self.STRING)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pbrtParser.STRING:
                self.state = 90 
                self.paramSet()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SamplerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramSet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ParamSetContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ParamSetContext,i)


        def SAMPLER(self):
            return self.getToken(pbrtParser.SAMPLER, 0)

        def STRING(self):
            return self.getToken(pbrtParser.STRING, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_sampler

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterSampler(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitSampler(self)




    def sampler(self):

        localctx = pbrtParser.SamplerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_sampler)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(self.SAMPLER)
            self.state = 97
            self.match(self.STRING)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pbrtParser.STRING:
                self.state = 98 
                self.paramSet()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PixelFilterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramSet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ParamSetContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ParamSetContext,i)


        def STRING(self):
            return self.getToken(pbrtParser.STRING, 0)

        def PIXELFILTER(self):
            return self.getToken(pbrtParser.PIXELFILTER, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_pixelFilter

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterPixelFilter(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitPixelFilter(self)




    def pixelFilter(self):

        localctx = pbrtParser.PixelFilterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_pixelFilter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(self.PIXELFILTER)
            self.state = 105
            self.match(self.STRING)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pbrtParser.STRING:
                self.state = 106 
                self.paramSet()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SurfaceIntegratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramSet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ParamSetContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ParamSetContext,i)


        def SURFACEINTEGRATOR(self):
            return self.getToken(pbrtParser.SURFACEINTEGRATOR, 0)

        def STRING(self):
            return self.getToken(pbrtParser.STRING, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_surfaceIntegrator

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterSurfaceIntegrator(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitSurfaceIntegrator(self)




    def surfaceIntegrator(self):

        localctx = pbrtParser.SurfaceIntegratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_surfaceIntegrator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(self.SURFACEINTEGRATOR)
            self.state = 113
            self.match(self.STRING)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pbrtParser.STRING:
                self.state = 114 
                self.paramSet()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CameraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramSet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ParamSetContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ParamSetContext,i)


        def CAMERA(self):
            return self.getToken(pbrtParser.CAMERA, 0)

        def STRING(self):
            return self.getToken(pbrtParser.STRING, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_camera

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterCamera(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitCamera(self)




    def camera(self):

        localctx = pbrtParser.CameraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_camera)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(self.CAMERA)
            self.state = 121
            self.match(self.STRING)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pbrtParser.STRING:
                self.state = 122 
                self.paramSet()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LookAtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOOKAT(self):
            return self.getToken(pbrtParser.LOOKAT, 0)

        def vector3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.Vector3Context)
            else:
                return self.getTypedRuleContext(pbrtParser.Vector3Context,i)


        def getRuleIndex(self):
            return pbrtParser.RULE_lookAt

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterLookAt(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitLookAt(self)




    def lookAt(self):

        localctx = pbrtParser.LookAtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_lookAt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(self.LOOKAT)
            self.state = 129 
            self.vector3()
            self.state = 130 
            self.vector3()
            self.state = 131 
            self.vector3()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(pbrtParser.EOF, 0)

        def body(self):
            return self.getTypedRuleContext(pbrtParser.BodyContext,0)


        def getRuleIndex(self):
            return pbrtParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitProgram(self)




    def program(self):

        localctx = pbrtParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133 
            self.body()
            self.state = 134
            self.match(self.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def film(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.FilmContext)
            else:
                return self.getTypedRuleContext(pbrtParser.FilmContext,i)


        def sampler(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.SamplerContext)
            else:
                return self.getTypedRuleContext(pbrtParser.SamplerContext,i)


        def concattransform(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ConcattransformContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ConcattransformContext,i)


        def scale(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ScaleContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ScaleContext,i)


        def surfaceIntegrator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.SurfaceIntegratorContext)
            else:
                return self.getTypedRuleContext(pbrtParser.SurfaceIntegratorContext,i)


        def worldBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.WorldBlockContext)
            else:
                return self.getTypedRuleContext(pbrtParser.WorldBlockContext,i)


        def renderer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.RendererContext)
            else:
                return self.getTypedRuleContext(pbrtParser.RendererContext,i)


        def pixelFilter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.PixelFilterContext)
            else:
                return self.getTypedRuleContext(pbrtParser.PixelFilterContext,i)


        def lookAt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.LookAtContext)
            else:
                return self.getTypedRuleContext(pbrtParser.LookAtContext,i)


        def camera(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.CameraContext)
            else:
                return self.getTypedRuleContext(pbrtParser.CameraContext,i)


        def translate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.TranslateContext)
            else:
                return self.getTypedRuleContext(pbrtParser.TranslateContext,i)


        def getRuleIndex(self):
            return pbrtParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitBody(self)




    def body(self):

        localctx = pbrtParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 147
                token = self._input.LA(1)
                if token in [self.TRANSLATE]:
                    self.state = 136 
                    self.translate()

                elif token in [self.CONCATTRANSFORM, self.PARAMSET_ITEM_LIST_START]:
                    self.state = 137 
                    self.concattransform()

                elif token in [self.SCALE]:
                    self.state = 138 
                    self.scale()

                elif token in [self.FILM]:
                    self.state = 139 
                    self.film()

                elif token in [self.RENDERER]:
                    self.state = 140 
                    self.renderer()

                elif token in [self.SAMPLER]:
                    self.state = 141 
                    self.sampler()

                elif token in [self.PIXELFILTER]:
                    self.state = 142 
                    self.pixelFilter()

                elif token in [self.SURFACEINTEGRATOR]:
                    self.state = 143 
                    self.surfaceIntegrator()

                elif token in [self.CAMERA]:
                    self.state = 144 
                    self.camera()

                elif token in [self.LOOKAT]:
                    self.state = 145 
                    self.lookAt()

                elif token in [self.WORLDBEGIN]:
                    self.state = 146 
                    self.worldBlock()

                else:
                    raise NoViableAltException(self)

                self.state = 149 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.CAMERA) | (1 << self.CONCATTRANSFORM) | (1 << self.FILM) | (1 << self.LOOKAT) | (1 << self.PIXELFILTER) | (1 << self.RENDERER) | (1 << self.SAMPLER) | (1 << self.SCALE) | (1 << self.SURFACEINTEGRATOR) | (1 << self.TRANSLATE) | (1 << self.WORLDBEGIN) | (1 << self.PARAMSET_ITEM_LIST_START))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WorldBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objectBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ObjectBlockContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ObjectBlockContext,i)


        def transform(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.TransformContext)
            else:
                return self.getTypedRuleContext(pbrtParser.TransformContext,i)


        def WORLDBEGIN(self):
            return self.getToken(pbrtParser.WORLDBEGIN, 0)

        def texture(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.TextureContext)
            else:
                return self.getTypedRuleContext(pbrtParser.TextureContext,i)


        def shape(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ShapeContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ShapeContext,i)


        def objectInstance(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ObjectInstanceContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ObjectInstanceContext,i)


        def WORLDEND(self):
            return self.getToken(pbrtParser.WORLDEND, 0)

        def material(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.MaterialContext)
            else:
                return self.getTypedRuleContext(pbrtParser.MaterialContext,i)


        def attributeBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.AttributeBlockContext)
            else:
                return self.getTypedRuleContext(pbrtParser.AttributeBlockContext,i)


        def getRuleIndex(self):
            return pbrtParser.RULE_worldBlock

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterWorldBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitWorldBlock(self)




    def worldBlock(self):

        localctx = pbrtParser.WorldBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_worldBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(self.WORLDBEGIN)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.ATTRIBUTEBEGIN) | (1 << self.MATERIAL) | (1 << self.OBJECTBEGIN) | (1 << self.OBJECTINSTANCE) | (1 << self.SHAPE) | (1 << self.TEXTURE) | (1 << self.TRANSFORM))) != 0):
                self.state = 159
                token = self._input.LA(1)
                if token in [self.OBJECTINSTANCE]:
                    self.state = 152 
                    self.objectInstance()

                elif token in [self.SHAPE]:
                    self.state = 153 
                    self.shape()

                elif token in [self.TEXTURE]:
                    self.state = 154 
                    self.texture()

                elif token in [self.MATERIAL]:
                    self.state = 155 
                    self.material()

                elif token in [self.TRANSFORM]:
                    self.state = 156 
                    self.transform()

                elif token in [self.ATTRIBUTEBEGIN]:
                    self.state = 157 
                    self.attributeBlock()

                elif token in [self.OBJECTBEGIN]:
                    self.state = 158 
                    self.objectBlock()

                else:
                    raise NoViableAltException(self)

                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 164
            self.match(self.WORLDEND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjectBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scale(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ScaleContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ScaleContext,i)


        def rotate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.RotateContext)
            else:
                return self.getTypedRuleContext(pbrtParser.RotateContext,i)


        def OBJECTEND(self):
            return self.getToken(pbrtParser.OBJECTEND, 0)

        def OBJECTBEGIN(self):
            return self.getToken(pbrtParser.OBJECTBEGIN, 0)

        def shape(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ShapeContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ShapeContext,i)


        def material(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.MaterialContext)
            else:
                return self.getTypedRuleContext(pbrtParser.MaterialContext,i)


        def translate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.TranslateContext)
            else:
                return self.getTypedRuleContext(pbrtParser.TranslateContext,i)


        def include(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.IncludeContext)
            else:
                return self.getTypedRuleContext(pbrtParser.IncludeContext,i)


        def attributeBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.AttributeBlockContext)
            else:
                return self.getTypedRuleContext(pbrtParser.AttributeBlockContext,i)


        def getRuleIndex(self):
            return pbrtParser.RULE_objectBlock

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterObjectBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitObjectBlock(self)




    def objectBlock(self):

        localctx = pbrtParser.ObjectBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_objectBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(self.OBJECTBEGIN)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.ATTRIBUTEBEGIN) | (1 << self.INCLUDE) | (1 << self.MATERIAL) | (1 << self.ROTATE) | (1 << self.SCALE) | (1 << self.SHAPE) | (1 << self.TRANSLATE))) != 0):
                self.state = 174
                token = self._input.LA(1)
                if token in [self.INCLUDE]:
                    self.state = 167 
                    self.include()

                elif token in [self.MATERIAL]:
                    self.state = 168 
                    self.material()

                elif token in [self.TRANSLATE]:
                    self.state = 169 
                    self.translate()

                elif token in [self.SCALE]:
                    self.state = 170 
                    self.scale()

                elif token in [self.ROTATE]:
                    self.state = 171 
                    self.rotate()

                elif token in [self.SHAPE]:
                    self.state = 172 
                    self.shape()

                elif token in [self.ATTRIBUTEBEGIN]:
                    self.state = 173 
                    self.attributeBlock()

                else:
                    raise NoViableAltException(self)

                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 179
            self.match(self.OBJECTEND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributeBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def areaLightSource(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.AreaLightSourceContext)
            else:
                return self.getTypedRuleContext(pbrtParser.AreaLightSourceContext,i)


        def scale(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ScaleContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ScaleContext,i)


        def rotate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.RotateContext)
            else:
                return self.getTypedRuleContext(pbrtParser.RotateContext,i)


        def ATTRIBUTEEND(self):
            return self.getToken(pbrtParser.ATTRIBUTEEND, 0)

        def shape(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ShapeContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ShapeContext,i)


        def ATTRIBUTEBEGIN(self):
            return self.getToken(pbrtParser.ATTRIBUTEBEGIN, 0)

        def lightSource(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.LightSourceContext)
            else:
                return self.getTypedRuleContext(pbrtParser.LightSourceContext,i)


        def material(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.MaterialContext)
            else:
                return self.getTypedRuleContext(pbrtParser.MaterialContext,i)


        def translate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.TranslateContext)
            else:
                return self.getTypedRuleContext(pbrtParser.TranslateContext,i)


        def include(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.IncludeContext)
            else:
                return self.getTypedRuleContext(pbrtParser.IncludeContext,i)


        def getRuleIndex(self):
            return pbrtParser.RULE_attributeBlock

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterAttributeBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitAttributeBlock(self)




    def attributeBlock(self):

        localctx = pbrtParser.AttributeBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_attributeBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(self.ATTRIBUTEBEGIN)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.AREALIGHTSOURCE) | (1 << self.INCLUDE) | (1 << self.LIGHTSOURCE) | (1 << self.MATERIAL) | (1 << self.ROTATE) | (1 << self.SCALE) | (1 << self.SHAPE) | (1 << self.TRANSLATE))) != 0):
                self.state = 190
                token = self._input.LA(1)
                if token in [self.INCLUDE]:
                    self.state = 182 
                    self.include()

                elif token in [self.MATERIAL]:
                    self.state = 183 
                    self.material()

                elif token in [self.AREALIGHTSOURCE]:
                    self.state = 184 
                    self.areaLightSource()

                elif token in [self.LIGHTSOURCE]:
                    self.state = 185 
                    self.lightSource()

                elif token in [self.ROTATE]:
                    self.state = 186 
                    self.rotate()

                elif token in [self.TRANSLATE]:
                    self.state = 187 
                    self.translate()

                elif token in [self.SCALE]:
                    self.state = 188 
                    self.scale()

                elif token in [self.SHAPE]:
                    self.state = 189 
                    self.shape()

                else:
                    raise NoViableAltException(self)

                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 195
            self.match(self.ATTRIBUTEEND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TransformBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def transform(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.TransformContext)
            else:
                return self.getTypedRuleContext(pbrtParser.TransformContext,i)


        def shape(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ShapeContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ShapeContext,i)


        def TRANSFORMEND(self):
            return self.getToken(pbrtParser.TRANSFORMEND, 0)

        def TRANSFORMBEGIN(self):
            return self.getToken(pbrtParser.TRANSFORMBEGIN, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_transformBlock

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterTransformBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitTransformBlock(self)




    def transformBlock(self):

        localctx = pbrtParser.TransformBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_transformBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(self.TRANSFORMBEGIN)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pbrtParser.SHAPE or _la==pbrtParser.TRANSFORM:
                self.state = 200
                token = self._input.LA(1)
                if token in [self.TRANSFORM]:
                    self.state = 198 
                    self.transform()

                elif token in [self.SHAPE]:
                    self.state = 199 
                    self.shape()

                else:
                    raise NoViableAltException(self)

                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 205
            self.match(self.TRANSFORMEND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TransformContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRANSFORM(self):
            return self.getToken(pbrtParser.TRANSFORM, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_transform

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterTransform(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitTransform(self)




    def transform(self):

        localctx = pbrtParser.TransformContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_transform)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(self.TRANSFORM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ShapeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramSet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ParamSetContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ParamSetContext,i)


        def SHAPE(self):
            return self.getToken(pbrtParser.SHAPE, 0)

        def STRING(self):
            return self.getToken(pbrtParser.STRING, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_shape

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterShape(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitShape(self)




    def shape(self):

        localctx = pbrtParser.ShapeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_shape)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(self.SHAPE)
            self.state = 210
            self.match(self.STRING)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pbrtParser.STRING:
                self.state = 211 
                self.paramSet()
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MaterialContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramSet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ParamSetContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ParamSetContext,i)


        def MATERIAL(self):
            return self.getToken(pbrtParser.MATERIAL, 0)

        def STRING(self):
            return self.getToken(pbrtParser.STRING, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_material

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterMaterial(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitMaterial(self)




    def material(self):

        localctx = pbrtParser.MaterialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_material)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(self.MATERIAL)
            self.state = 218
            self.match(self.STRING)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pbrtParser.STRING:
                self.state = 219 
                self.paramSet()
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RotateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROTATE(self):
            return self.getToken(pbrtParser.ROTATE, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_rotate

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterRotate(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitRotate(self)




    def rotate(self):

        localctx = pbrtParser.RotateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_rotate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(self.ROTATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LightSourceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramSet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ParamSetContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ParamSetContext,i)


        def LIGHTSOURCE(self):
            return self.getToken(pbrtParser.LIGHTSOURCE, 0)

        def STRING(self):
            return self.getToken(pbrtParser.STRING, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_lightSource

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterLightSource(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitLightSource(self)




    def lightSource(self):

        localctx = pbrtParser.LightSourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_lightSource)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(self.LIGHTSOURCE)
            self.state = 228
            self.match(self.STRING)
            self.state = 230 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 229 
                self.paramSet()
                self.state = 232 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==pbrtParser.STRING):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TranslateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(pbrtParser.NUMBER)
            else:
                return self.getToken(pbrtParser.NUMBER, i)

        def TRANSLATE(self):
            return self.getToken(pbrtParser.TRANSLATE, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_translate

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterTranslate(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitTranslate(self)




    def translate(self):

        localctx = pbrtParser.TranslateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_translate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(self.TRANSLATE)
            self.state = 235
            self.match(self.NUMBER)
            self.state = 236
            self.match(self.NUMBER)
            self.state = 237
            self.match(self.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ScaleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCALE(self):
            return self.getToken(pbrtParser.SCALE, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(pbrtParser.NUMBER)
            else:
                return self.getToken(pbrtParser.NUMBER, i)

        def getRuleIndex(self):
            return pbrtParser.RULE_scale

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterScale(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitScale(self)




    def scale(self):

        localctx = pbrtParser.ScaleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_scale)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(self.SCALE)
            self.state = 240
            self.match(self.NUMBER)
            self.state = 241
            self.match(self.NUMBER)
            self.state = 242
            self.match(self.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AreaLightSourceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramSet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ParamSetContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ParamSetContext,i)


        def AREALIGHTSOURCE(self):
            return self.getToken(pbrtParser.AREALIGHTSOURCE, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_areaLightSource

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterAreaLightSource(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitAreaLightSource(self)




    def areaLightSource(self):

        localctx = pbrtParser.AreaLightSourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_areaLightSource)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(self.AREALIGHTSOURCE)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pbrtParser.STRING:
                self.state = 245 
                self.paramSet()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TextureContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramSet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ParamSetContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ParamSetContext,i)


        def TEXTURE(self):
            return self.getToken(pbrtParser.TEXTURE, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_texture

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterTexture(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitTexture(self)




    def texture(self):

        localctx = pbrtParser.TextureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_texture)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(self.TEXTURE)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pbrtParser.STRING:
                self.state = 252 
                self.paramSet()
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IncludeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCLUDE(self):
            return self.getToken(pbrtParser.INCLUDE, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_include

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterInclude(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitInclude(self)




    def include(self):

        localctx = pbrtParser.IncludeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_include)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(self.INCLUDE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjectInstanceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramSet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pbrtParser.ParamSetContext)
            else:
                return self.getTypedRuleContext(pbrtParser.ParamSetContext,i)


        def OBJECTINSTANCE(self):
            return self.getToken(pbrtParser.OBJECTINSTANCE, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_objectInstance

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterObjectInstance(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitObjectInstance(self)




    def objectInstance(self):

        localctx = pbrtParser.ObjectInstanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_objectInstance)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(self.OBJECTINSTANCE)
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pbrtParser.STRING:
                self.state = 261 
                self.paramSet()
                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConcattransformContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(pbrtParser.STRING)
            else:
                return self.getToken(pbrtParser.STRING, i)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(pbrtParser.NUMBER)
            else:
                return self.getToken(pbrtParser.NUMBER, i)

        def CONCATTRANSFORM(self):
            return self.getToken(pbrtParser.CONCATTRANSFORM, 0)

        def getRuleIndex(self):
            return pbrtParser.RULE_concattransform

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.enterConcattransform(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, pbrtListener ):
                listener.exitConcattransform(self)




    def concattransform(self):

        localctx = pbrtParser.ConcattransformContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_concattransform)
        self._la = 0 # Token type
        try:
            self.state = 282
            token = self._input.LA(1)
            if token in [self.CONCATTRANSFORM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(self.CONCATTRANSFORM)

                self.state = 268
                self.match(self.PARAMSET_ITEM_LIST_START)
                self.state = 270 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 269
                    self.match(self.NUMBER)
                    self.state = 272 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==pbrtParser.NUMBER):
                        break

                self.state = 274
                self.match(self.PARAMSET_ITEM_LIST_END)

            elif token in [self.PARAMSET_ITEM_LIST_START]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.match(self.PARAMSET_ITEM_LIST_START)
                self.state = 277 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 276
                    self.match(self.STRING)
                    self.state = 279 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==pbrtParser.STRING):
                        break

                self.state = 281
                self.match(self.PARAMSET_ITEM_LIST_END)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




