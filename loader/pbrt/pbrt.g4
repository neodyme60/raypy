grammar pbrt;

// ***************** lexer rules:
STRING : '"' ('a'..'z'|'A'..'Z'|'0'..'9'|'_'|'-'|' '|'.'|'-')+ '"';
INT
    :   (DecimalIntegerLiteral
    |   HexIntegerLiteral
    |   OctalIntegerLiteral
    |   BinaryIntegerLiteral)
    ;

FLOAT
    :   (DecimalFloatingPointLiteral
    |   HexadecimalFloatingPointLiteral)
    ;


fragment DecimalIntegerLiteral : DecimalNumeral IntegerTypeSuffix?;
fragment Digits : Digit (DigitOrUnderscore* Digit)?;
fragment HexadecimalFloatingPointLiteral : HexSignificand BinaryExponent FloatTypeSuffix?;
fragment HexIntegerLiteral : HexNumeral IntegerTypeSuffix?;
fragment OctalNumeral : '0' Underscores? OctalDigits;
fragment Underscores : '_'+;
fragment OctalDigits : OctalDigit (OctalDigitOrUnderscore* OctalDigit)?;
fragment OctalDigit : [0-7];
fragment OctalDigitOrUnderscore : OctalDigit | '_';
fragment OctalIntegerLiteral : OctalNumeral IntegerTypeSuffix?;
fragment BinaryIntegerLiteral : BinaryNumeral IntegerTypeSuffix?;
fragment BinaryNumeral : '0' [bB] BinaryDigits ;
fragment BinaryDigits : BinaryDigit (BinaryDigitOrUnderscore* BinaryDigit)?;
fragment BinaryDigit : [01];
fragment BinaryDigitOrUnderscore : BinaryDigit | '_';
fragment IntegerTypeSuffix : [lL];
fragment DecimalNumeral : '0' | NonZeroDigit (Digits? | Underscores Digits);
fragment HexSignificand : HexNumeral '.'? | '0' [xX] HexDigits? '.' HexDigits;
fragment BinaryExponent : BinaryExponentIndicator SignedInteger;
fragment BinaryExponentIndicator : [pP];
fragment HexNumeral : '0' [xX] HexDigits;
fragment HexDigits : HexDigit (HexDigitOrUnderscore* HexDigit)?;
fragment HexDigit : [0-9a-fA-F];
fragment HexDigitOrUnderscore : HexDigit | '_';
fragment DecimalFloatingPointLiteral
    :   Digits '.' Digits? ExponentPart? FloatTypeSuffix?
    |   '.' Digits ExponentPart? FloatTypeSuffix?
    |   Digits ExponentPart FloatTypeSuffix?
    |   Digits FloatTypeSuffix
    ;
fragment ExponentPart : ExponentIndicator SignedInteger;
fragment ExponentIndicator : [eE];
fragment SignedInteger : Sign? Digits;
fragment Sign : [+-];
fragment DigitOrUnderscore : Digit | '_';
fragment Digit : '0' | NonZeroDigit;
fragment NonZeroDigit : [1-9];
fragment FloatTypeSuffix : [fFdD];

WS : [ \t\r\n]+ -> skip;
Comment: '#' ~( '\r' | '\n' )*;

ACCELERATOR : 'Accelerator';
ACTIVETRANSFORM : 'ActiveTransform';
ALL : 'All';
AREALIGHTSOURCE: 'AreaLightSource';
ATTRIBUTEBEGIN: 'AttributeBegin';
ATTRIBUTEEND:'AttributeEnd';
CAMERA:'Camera';
CONCATTRANSFORM:'ConcatTransform';
COORDINATESYSTEM:'CoordinateSystem';
COORDSYSTRANSFORM: 'CoordSysTransform';
ENDTIME:'EndTime';
FILM:'Film';
IDENTITY:'Identity';
INCLUDE:'Include';
LIGHTSOURCE:'LightSource';
LOOKAT:'LookAt';
MAKENAMEDMATERIAL:'MakeNamedMaterial';
MATERIAL:'Material';
NAMEDMATERIAL:'NamedMaterial';
OBJECTBEGIN:'ObjectBegin';
OBJECTEND:'ObjectEnd';
OBJECTINSTANCE:'ObjectInstance';
PIXELFILTER:'PixelFilter';
RENDERER:'Renderer';
REVERSEORIENTATION:'ReverseOrientation';
ROTATE:'Rotate';
SAMPLER:'Sampler';
SCALE:'Scale';
SHAPE:'Shape';
STARTTIME:'StartTime';
SURFACEINTEGRATOR:'SurfaceIntegrator';
TEXTURE:'Texture';
TRANSFORMBEGIN:'TransformBegin';
TRANSFORMEND:'TransformEnd';
TRANSFORMTIMES:'TransformTimes';
TRANSFORM:'Transform';
TRANSLATE:'Translate';
VOLUME:'Volume';
VOLUMEINTEGRATOR:'VolumeIntegrator';
WORLDBEGIN:'WorldBegin';
WORLDEND:'WorldEnd';
PARAMSET_ITEM_LIST_START: '[';
PARAMSET_ITEM_LIST_END: ']';

// ***************** parser rules:
vector3: FLOAT FLOAT FLOAT;
paramsetitem: ( FLOAT | INT | STRING);
paramset: STRING (paramsetitem | ((PARAMSET_ITEM_LIST_START  paramsetitem+ PARAMSET_ITEM_LIST_END)));

film: FILM STRING paramset*;
sampler: SAMPLER STRING paramset*;
pixelFilter: PIXELFILTER STRING paramset*;
surfaceIntegrator: SURFACEINTEGRATOR STRING paramset*;
camera: CAMERA STRING paramset*;
lookAt: LOOKAT vector3 vector3 vector3;
program: body EOF;
body: ( film | sampler | pixelFilter | surfaceIntegrator | camera | lookAt | worldBlock )+;
worldBlock: WORLDBEGIN ( objectInstance | shape | texture | material | transform | attributeBlock | objectBlock )* WORLDEND;        
objectBlock: OBJECTBEGIN ( include | material | translate | scale | rotate | shape | attributeBlock )* OBJECTEND;
attributeBlock: ATTRIBUTEBEGIN ( include | areaLightSource | lightSource | rotate | translate | scale | shape)* ATTRIBUTEEND;
transformBlock: TRANSFORMBEGIN ( transform | shape )* TRANSFORMEND;
transform: TRANSFORM;
shape: SHAPE STRING paramset*;
material: MATERIAL paramset*;
rotate: ROTATE;
lightSource: LIGHTSOURCE;
translate : TRANSLATE FLOAT FLOAT FLOAT;
scale: SCALE;
areaLightSource: AREALIGHTSOURCE paramset*;
texture: TEXTURE paramset*;
include: INCLUDE;
objectInstance: OBJECTINSTANCE paramset*;
