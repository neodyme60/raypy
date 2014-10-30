SET CLASSPATH=.;antlr-4.4-complete.jar;%CLASSPATH%
doskey antlr4=java org.antlr.v4.Tool $*  -Dlanguage=Python3
doskey grun =java org.antlr.v4.runtime.misc.TestRig $*  -Dlanguage=Python3 --rule=start-rule
