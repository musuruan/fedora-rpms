#!/usr/bin/sh
GAME=hydracastlelabyrinth
GAME_LOCAL_DIR=$HOME/.hcl
GAME_DATA_DIR=/usr/share/$GAME
GAME_EXECUTABLE=/usr/libexec/hcl
mkdir -p $GAME_LOCAL_DIR
cd $GAME_LOCAL_DIR
ln -snf $GAME_DATA_DIR/data data
exec $GAME_EXECUTABLE "$@"

