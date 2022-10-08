#delete folder if exists
rm -rf nightlytorch

#remove old nightlytorch
poetry remove torch torchvision torchaudio

pip download --no-deps --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu --dest nightlytorch/

# run poetry add for every file in nightlytorch
for file in nightlytorch/*.whl; do
    poetry add $file
done