#!/bin/sh -e
# $Id$

[ -r /usr/share/java-utils/java-functions ] || exit 1

. /usr/share/java-utils/java-functions

jars="yuicompressor"
CLASSPATH=$(build-classpath $jars)
MAIN_CLASS=com.yahoo.platform.yui.compressor.Bootstrap

run ${1:+$@}
