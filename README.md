# AstroClock

## Troubleshooting

- numpy 1.14.3 can't open libf77blas.so.3 on Raspberry Pi Zero W (arm6)

you need to remove the numpy zheel package and get it from the raspbian repos instead:

```
pip3 uninstall numpy #remove previously installed package
apt install python3-numpy
```

more details at https://github.com/numpy/numpy/issues/11110#issuecomment-460026078
