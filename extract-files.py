#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/sm8450-common',
    'hardware/qcom-caf/sm8450',
    'hardware/xiaomi',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/xiaomi/sm8450-common',
]

blob_fixups: blob_fixups_user_type = {
    (
        'vendor/etc/camera/zizhan_enhance_motiontuning.xml',
        'vendor/etc/camera/zizhan_motiontuning.xml',
    ): blob_fixup().regex_replace('xml=version', 'xml version'),
    ('vendor/etc/camera/pureView_parameter.xml',): blob_fixup().regex_replace(
        r'=([0-9]+)>', r'="\1">'
    ),
    'vendor/lib64/hw/camera.xiaomi.so': blob_fixup()
    .add_needed('libprocessgroup_shim.so')
    .update_graphic_buffer_size(
        [
            '_ZN5mihal9GraBufferC2EjjimNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE',
            '_ZN5mihal9GraBufferC2EPKNS_6StreamENSt3__112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE',
            '_ZN5mihal9GraBufferC2EjjimPK13native_handle',
            '_ZN5mihal9GraBufferC2EPKNS_6StreamEPK13native_handle',
        ],
    ),
    (
        'vendor/lib64/hw/com.qti.chi.override.so',
        'vendor/lib64/libcamxcommonutils.so',
        'vendor/lib64/libmialgoengine.so',
    ): blob_fixup().add_needed('libprocessgroup_shim.so'),
    (
        'vendor/lib64/libTrueSight.so',
        'vendor/lib64/libarcsoft_beautyshot.so',
    ): blob_fixup()
    .clear_symbol_version('AHardwareBuffer_allocate')
    .clear_symbol_version('AHardwareBuffer_describe')
    .clear_symbol_version('AHardwareBuffer_isSupported')
    .clear_symbol_version('AHardwareBuffer_lock')
    .clear_symbol_version('AHardwareBuffer_lockPlanes')
    .clear_symbol_version('AHardwareBuffer_release')
    .clear_symbol_version('AHardwareBuffer_unlock'),
    'vendor/lib64/libcamximageformatutils.so': blob_fixup().replace_needed(
        'vendor.qti.hardware.display.config-V2-ndk_platform.so',
        'vendor.qti.hardware.display.config-V2-ndk.so',
    ),
    'vendor/lib64/libcom.xiaomi.grallocutils.so': blob_fixup().update_graphic_buffer_size(
        [
            '_Z21allocateGraphicBufferjjim',
            '_Z29createGraphicBufferFromHandlejjimjPK13native_handle',
            '_ZN12GrallocUtils19createGrallocBufferEjjimjPK13native_handleP16GrallocBufHandle',
        ],
    ),

}

module = ExtractUtilsModule(
    'zizhan',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8450-common', module.vendor
    )
    utils.run()
