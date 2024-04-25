# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import numpy as np

import paddle
from paddle import base
from paddle.base import core


def np_sinc(x: np.ndarray):
    return np.sinc(x)


class TestSincAPI(unittest.TestCase):
    def setUp(self):
        self.cpu_support_dtypes = [
            'float32',
            'float64',
        ]
        self.cuda_support_dtypes = [
            'float32',
            'float64',
        ]
        self.place = [paddle.CPUPlace()]
        if core.is_compiled_with_cuda():
            self.place.append(paddle.CUDAPlace(0))
        self.shapes = [[6], [16, 64]]

    def test_dtype(self):
        def run_dygraph(place):
            paddle.disable_static(place)
            if core.is_compiled_with_cuda():
                support_dtypes = self.cuda_support_dtypes
            else:
                support_dtypes = self.cpu_support_dtypes

            for dtype in support_dtypes:
                for shape in self.shapes:
                    x_data = np.random.rand(*shape).astype(dtype)
                    x = paddle.to_tensor(x_data)
                    out = paddle.sinc(x)
                    out_expected = np_sinc(x_data)
                    np.testing.assert_allclose(
                        out.numpy(), out_expected, rtol=1e-6, atol=1e-6
                    )

        def run_static(place):
            paddle.enable_static()
            if core.is_compiled_with_cuda():
                support_dtypes = self.cuda_support_dtypes
            else:
                support_dtypes = self.cpu_support_dtypes
            for dtype in support_dtypes:
                for shape in self.shapes:
                    x_data = np.random.rand(*shape).astype(dtype)
                    startup_program = paddle.static.Program()
                    main_program = paddle.static.Program()
                    exe = base.Executor(place)
                    with paddle.static.program_guard(
                        main_program, startup_program
                    ):
                        x = paddle.static.data(
                            name='x', shape=shape, dtype=dtype
                        )
                        res = paddle.sinc(x)
                        static_result = exe.run(
                            feed={'x': x_data}, fetch_list=[res]
                        )[0]
                        out_expected = np_sinc(x_data)
                    np.testing.assert_allclose(
                        static_result, out_expected, rtol=1e-6, atol=1e-6
                    )

        for place in self.place:
            run_dygraph(place)
            run_static(place)

    def test_zero(self):
        def run_dygraph(place):
            paddle.disable_static(place)
            if core.is_compiled_with_cuda():
                support_dtypes = self.cuda_support_dtypes
            else:
                support_dtypes = self.cpu_support_dtypes

            for dtype in support_dtypes:
                for shape in self.shapes:
                    x_data = np.random.rand(*shape).astype(dtype)
                    mask = (
                        (np.random.rand(*shape) > 0.5)
                        .astype('int')
                        .astype(dtype)
                    )
                    x_data = x_data * mask
                    x = paddle.to_tensor(x_data)
                    out = paddle.sinc(x)
                    out_expected = np_sinc(x_data)
                    np.testing.assert_allclose(
                        out.numpy(), out_expected, rtol=1e-6, atol=1e-6
                    )

        for place in self.place:
            run_dygraph(place)

    def test_input_type_error(self):
        with self.assertRaises(TypeError):
            x = np.random.rand(6).astype('float32')
            x = paddle.sinc(x)

    def test_input_dype_error(self):
        paddle.enable_static()
        place = paddle.CPUPlace()
        with self.assertRaises(TypeError):
            x_data = np.random.rand(6).astype('int32')
            startup_program = paddle.static.Program()
            main_program = paddle.static.Program()
            exe = base.Executor(place)
            with paddle.static.program_guard(main_program, startup_program):
                x = paddle.static.data(name='x', shape=[6], dtype='int32')
                res = paddle.sinc(x)
                static_result = exe.run(feed={'x': x_data}, fetch_list=[res])[0]

        with self.assertRaises(TypeError):
            x_data = np.random.rand(6).astype('int64')
            startup_program = paddle.static.Program()
            main_program = paddle.static.Program()
            exe = base.Executor(place)
            with paddle.static.program_guard(main_program, startup_program):
                x = paddle.static.data(name='x', shape=[6], dtype='int64')
                res = paddle.sinc(x)
                static_result = exe.run(feed={'x': x_data}, fetch_list=[res])[0]


class TestSincInplaceAPI(unittest.TestCase):
    def setUp(self):
        self.cpu_support_dtypes = [
            'float32',
            'float64',
        ]
        self.cuda_support_dtypes = [
            'float32',
            'float64',
        ]
        self.place = [paddle.CPUPlace()]
        if core.is_compiled_with_cuda():
            self.place.append(paddle.CUDAPlace(0))
        self.shapes = [[6], [16, 64]]

    def test_inplace(self):
        def run_dygraph(place):
            paddle.disable_static(place)
            if core.is_compiled_with_cuda():
                support_dtypes = self.cuda_support_dtypes
            else:
                support_dtypes = self.cpu_support_dtypes

            for dtype in support_dtypes:
                for shape in self.shapes:
                    x_data = np.random.rand(*shape).astype(dtype)
                    x = paddle.to_tensor(x_data)
                    paddle.sinc_(x)
                    out_expected = np_sinc(x_data)
                    np.testing.assert_allclose(
                        x.numpy(), out_expected, rtol=1e-6, atol=1e-6
                    )

        for place in self.place:
            run_dygraph(place)

    def test_inplace_input_type_error(self):
        with self.assertRaises(TypeError):
            x = np.random.rand(6).astype('float32')
            paddle.sinc_(x)


@unittest.skipIf(
    not core.is_compiled_with_cuda()
    or not core.is_float16_supported(core.CUDAPlace(0)),
    "core is not compiled with CUDA and not support the float16",
)
class TestSincAPIFP16(unittest.TestCase):
    def setUp(self):
        self.shapes = [[6], [16, 64]]
        self.dtype = 'float16'
        self.place = paddle.CUDAPlace(0)

    def test_dtype(self):
        def run_static(place):
            paddle.enable_static()
            for shape in self.shapes:
                x_data = np.random.rand(*shape).astype(self.dtype)
                startup_program = paddle.static.Program()
                main_program = paddle.static.Program()
                exe = base.Executor(place)
                with paddle.static.program_guard(main_program, startup_program):
                    x = paddle.static.data(
                        name='x', shape=shape, dtype=self.dtype
                    )
                    res = paddle.sinc(x)
                    static_result = exe.run(
                        feed={'x': x_data}, fetch_list=[res]
                    )[0]
                    out_expected = np_sinc(x_data)
                np.testing.assert_allclose(
                    static_result, out_expected, rtol=1e-6, atol=1e-6
                )

        run_static(self.place)


if __name__ == "__main__":
    unittest.main()
