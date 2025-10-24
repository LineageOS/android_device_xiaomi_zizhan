#
# Copyright (C) 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Security patch level
VENDOR_SECURITY_PATCH := 2025-10-01

# Inherit from xiaomi sm8450-common
include device/xiaomi/sm8450-common/BoardConfigCommon.mk

# Inherit from the proprietary version
include vendor/xiaomi/zizhan/BoardConfigVendor.mk

DEVICE_PATH := device/xiaomi/zizhan

# Audio
AUDIO_FEATURE_ENABLED_CIRRUS_CALIBRATION_RESISTANCE := true

# Kernel
device_second_stage_modules := \
    fst2.ko

BOARD_VENDOR_RAMDISK_RECOVERY_KERNEL_MODULES_LOAD += $(device_second_stage_modules)
BOARD_VENDOR_KERNEL_MODULES_LOAD += $(device_second_stage_modules)

BOOT_KERNEL_MODULES += $(device_second_stage_modules)

# Properties
TARGET_SYSTEM_PROP += $(DEVICE_PATH)/properties/system.prop
TARGET_VENDOR_PROP += $(DEVICE_PATH)/properties/vendor.prop

# Recovery
TARGET_RECOVERY_DEFAULT_ROTATION := ROTATION_LEFT

# Screen density
TARGET_SCREEN_DENSITY := 440

# Properties
TARGET_VENDOR_PROP += $(DEVICE_PATH)/vendor.prop
