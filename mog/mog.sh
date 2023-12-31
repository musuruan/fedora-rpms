#!/bin/sh
GAME=mog
GAME_LOCAL_DIR=$HOME/.$GAME
GAME_DATA_DIR=/usr/share/$GAME
GAME_EXECUTABLE=/usr/libexec/$GAME/$GAME
mkdir -p $GAME_LOCAL_DIR
cd $GAME_LOCAL_DIR
for dir in graphics rooms sound; do
ln -snf $GAME_DATA_DIR/$dir $dir
done
exec $GAME_EXECUTABLE "$@"

