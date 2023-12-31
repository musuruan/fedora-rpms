#!/bin/sh
GAME_LOCAL_DIR=$HOME/.crates
GAME_DATA_DIR=/usr/share/crates
GAME_EXECUTABLE=/usr/libexec/crates/crates
mkdir -p $GAME_LOCAL_DIR/resources
cd $GAME_LOCAL_DIR
cd resources
for dir in `find  $GAME_DATA_DIR/resources/ -maxdepth 1 -type d -exec basename {} \;`
do
ln -snf $GAME_DATA_DIR/resources/$dir $dir
done
test -e config.lua || cp $GAME_DATA_DIR/resources/config.lua config.lua
cd ..
cp -a $GAME_EXECUTABLE crates
exec ./crates "$@"

