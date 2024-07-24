/* Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. */

#pragma once

#include "paddle/phi/core/dense_tensor.h"

namespace phi {

template <typename T, typename Context>
void MatrixRankKernel(const Context& dev_ctx,
                      const DenseTensor& x,
                      float tol,
                      bool use_default_tol,
                      bool hermitian,
                      DenseTensor* out);

template <typename T, typename Context>
void MatrixRank2Kernel(const Context& dev_ctx,
                       const DenseTensor& x,
                       float atol,
                       float rtol,
                       bool use_default_tol,
                       bool hermitian,
                       DenseTensor* out);

template <typename T, typename Context>
void MatrixRankAtolKernel(const Context& dev_ctx,
                          const DenseTensor& x,
                          const DenseTensor& atol_tensor,
                          float rtol,
                          bool hermitian,
                          DenseTensor* out);

template <typename T, typename Context>
void MatrixRankRtolKernel(const Context& dev_ctx,
                          const DenseTensor& x,
                          const DenseTensor& rtol_tensor,
                          float atol,
                          bool hermitian,
                          DenseTensor* out);

}  // namespace phi
