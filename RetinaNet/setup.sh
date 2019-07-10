echo "Setup datasets"
cd keras_retinanet && mkdir VOCdevkit2007 && cd VOCdevkit2007 && ln -s $PAI_DATA_DIR
cd ../..
echo "Done!"