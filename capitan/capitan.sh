#!/bin/sh
GAME=capitan
GAME_DATA_DIR=/usr/share/$GAME
GAME_EXECUTABLE=/usr/libexec/$GAME/$GAME
cd $GAME_DATA_DIR
exec $GAME_EXECUTABLE

