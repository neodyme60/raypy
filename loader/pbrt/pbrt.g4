grammar pbrt;

    
// ***************** lexer rules:
STRING:  '"' ('a'..'z'|'A'..'Z'|'0'..'9'|'_'|'-'|'.'|'-'|' ')+ '"';
fragment Exponent : ('e'|'E') ('+'|'-')? ('0'..'9')+ ;
NUMBER: ((('+'|'-')?('1'..'9')?('0'..'9')+('.'('0'..'9')+)?)|('.'('0'..'9')+))Exponent?;

WS : [ \t\r\n]+ -> skip;
LINE_COMMENT: '#' ~( '\r' | '\n' )*  -> skip;

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

vector3: NUMBER NUMBER NUMBER;
paramSetLeft: STRING;
paramSet: paramSetLeft (STRING | ('[' (NUMBER)+ ']') | ('[' (STRING)+ ']') );

film: FILM STRING paramSet*;
renderer: RENDERER STRING paramSet*;
sampler: SAMPLER STRING paramSet*;
pixelFilter: PIXELFILTER  STRING paramSet*;
surfaceIntegrator: SURFACEINTEGRATOR STRING paramSet*;
camera: CAMERA STRING paramSet*;
lookAt: LOOKAT vector3 vector3 vector3;
program: body EOF;
body: ( accelerator | transformBlock | translate | concattransform | scale | film | renderer | sampler | pixelFilter | surfaceIntegrator | camera | lookAt | worldBlock )+;
worldBlock: WORLDBEGIN ( transformBlock | objectInstance | shape | texture | material | namedmaterial | makenamedmaterial | transform | attributeBlock | objectBlock )* WORLDEND;        
objectBlock: OBJECTBEGIN ( include | material | namedmaterial | makenamedmaterial | translate | scale | rotate | shape | attributeBlock )* OBJECTEND;
attributeBlock: ATTRIBUTEBEGIN ( arealightsource | include | material | namedmaterial | makenamedmaterial | areaLightSource | lightSource | rotate | translate | scale | shape)* ATTRIBUTEEND;
transformBlock: TRANSFORMBEGIN ( translate | transform | shape )* TRANSFORMEND;
transform: TRANSFORM;
shape: SHAPE STRING paramSet*;
material: MATERIAL STRING paramSet*;
namedmaterial: NAMEDMATERIAL STRING;
makenamedmaterial: MAKENAMEDMATERIAL STRING paramSet*;
arealightsource: AREALIGHTSOURCE STRING paramSet*;
rotate: ROTATE;
lightSource: LIGHTSOURCE STRING paramSet+;
accelerator: ACCELERATOR STRING paramSet+;
translate : TRANSLATE NUMBER NUMBER NUMBER;
scale: SCALE NUMBER NUMBER NUMBER;
areaLightSource: AREALIGHTSOURCE paramSet*;
texture: TEXTURE paramSet*;
include: INCLUDE;
objectInstance: OBJECTINSTANCE paramSet*;
concattransform: CONCATTRANSFORM ('[' (NUMBER)+ ']') | ('[' (STRING)+ ']');
