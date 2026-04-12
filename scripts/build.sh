DIST="./dist"

if [ ! -d "$DIST" ]; then
    mkdir "$DIST"
fi

cp main.py "$DIST/"