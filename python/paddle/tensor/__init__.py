# Copyright (c) 2016 PaddlePaddle Authors. All Rights Reserved
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

from ..signal import (  # noqa: F401
    istft,
    stft,
)
from .array import (  # noqa: F401
    array_length,
    array_read,
    array_write,
    create_array,
)
from .attribute import (  # noqa: F401
    imag,
    is_complex,
    is_floating_point,
    is_integer,
    rank,
    real,
    shape,
)
from .creation import (  # noqa: F401
    arange,
    cauchy_,
    complex,
    create_parameter,
    create_tensor,
    diag,
    diag_embed,
    diagflat,
    empty,
    empty_like,
    eye,
    fill_constant,
    full,
    full_like,
    geometric_,
    linspace,
    meshgrid,
    ones,
    ones_like,
    polar,
    set_,
    to_tensor,
    tril,
    tril_,
    triu,
    triu_,
    zeros,
    zeros_like,
)
from .einsum import einsum  # noqa: F401
from .linalg import (  # noqa: F401
    bincount,
    bmm,
    cdist,
    cholesky,
    cholesky_inverse,
    cholesky_solve,
    cond,
    corrcoef,
    cov,
    cross,
    dist,
    dot,
    eig,
    eigh,
    eigvals,
    eigvalsh,
    histogram,
    histogram_bin_edges,
    histogramdd,
    householder_product,
    lstsq,
    lu,
    lu_unpack,
    matmul,
    matrix_power,
    multi_dot,
    mv,
    norm,
    ormqr,
    pca_lowrank,
    pinv,
    qr,
    solve,
    svd,
    svd_lowrank,
    t,
    t_,
    transpose,
    transpose_,
)
from .logic import (  # noqa: F401
    allclose,
    bitwise_and,
    bitwise_and_,
    bitwise_not,
    bitwise_not_,
    bitwise_or,
    bitwise_or_,
    bitwise_xor,
    bitwise_xor_,
    equal,
    equal_,
    equal_all,
    greater_equal,
    greater_equal_,
    greater_than,
    greater_than_,
    is_empty,
    is_tensor,
    isclose,
    less_equal,
    less_equal_,
    less_than,
    less_than_,
    logical_and,
    logical_and_,
    logical_not,
    logical_not_,
    logical_or,
    logical_or_,
    logical_xor,
    logical_xor_,
    not_equal,
    not_equal_,
)
from .manipulation import (  # noqa: F401
    as_complex,
    as_real,
    as_strided,
    atleast_1d,
    atleast_2d,
    atleast_3d,
    block_diag,
    broadcast_tensors,
    broadcast_to,
    cast,
    cast_,
    chunk,
    column_stack,
    concat,
    diagonal_scatter,
    dsplit,
    dstack,
    expand,
    expand_as,
    flatten,
    flatten_,
    flip,
    flip as reverse,
    gather,
    gather_nd,
    hsplit,
    hstack,
    index_add,
    index_add_,
    index_fill,
    index_fill_,
    index_put,
    index_put_,
    masked_fill,
    masked_fill_,
    masked_scatter,
    masked_scatter_,
    moveaxis,
    put_along_axis,
    put_along_axis_,
    repeat_interleave,
    reshape,
    reshape_,
    roll,
    rot90,
    row_stack,
    scatter,
    scatter_,
    scatter_nd,
    scatter_nd_add,
    select_scatter,
    shard_index,
    slice,
    slice_scatter,
    split,
    squeeze,
    squeeze_,
    stack,
    strided_slice,
    take_along_axis,
    tensor_split,
    tensordot,
    tile,
    unbind,
    unflatten,
    unfold,
    unique,
    unique_consecutive,
    unsqueeze,
    unsqueeze_,
    unstack,
    view,
    view_as,
    vsplit,
    vstack,
)
from .math import (  # noqa: F401
    abs,
    abs_,
    acos,
    acos_,
    acosh,
    acosh_,
    add,
    add_,
    add_n,
    addmm,
    addmm_,
    all,
    amax,
    amin,
    angle,
    any,
    asin,
    asin_,
    asinh,
    asinh_,
    atan,
    atan2,
    atan_,
    atanh,
    atanh_,
    bitwise_left_shift,
    bitwise_left_shift_,
    bitwise_right_shift,
    bitwise_right_shift_,
    broadcast_shape,
    cartesian_prod,
    ceil,
    ceil_,
    clip,
    clip_,
    combinations,
    conj,
    copysign,
    copysign_,
    cos,
    cos_,
    cosh,
    cosh_,
    count_nonzero,
    cummax,
    cummin,
    cumprod,
    cumprod_,
    cumsum,
    cumsum_,
    cumulative_trapezoid,
    deg2rad,
    diagonal,
    diff,
    digamma,
    digamma_,
    divide,
    divide_,
    erf,
    erfinv,
    erfinv_,
    exp,
    exp_,
    expm1,
    floor,
    floor_,
    floor_divide,
    floor_divide_,
    floor_mod,
    floor_mod_,
    fmax,
    fmin,
    frac,
    frac_,
    frexp,
    gammainc,
    gammainc_,
    gammaincc,
    gammaincc_,
    gammaln,
    gammaln_,
    gcd,
    gcd_,
    heaviside,
    hypot,
    hypot_,
    i0,
    i0_,
    i0e,
    i1,
    i1e,
    increment,
    inner,
    inverse,
    isfinite,
    isin,
    isinf,
    isnan,
    isneginf,
    isposinf,
    isreal,
    kron,
    lcm,
    lcm_,
    ldexp,
    ldexp_,
    lerp,
    lerp_,
    lgamma,
    lgamma_,
    log,
    log1p,
    log1p_,
    log2,
    log2_,
    log10,
    log10_,
    log_,
    logaddexp,
    logcumsumexp,
    logit,
    logit_,
    logsumexp,
    max,
    maximum,
    min,
    minimum,
    mm,
    mod,
    mod_,
    multigammaln,
    multigammaln_,
    multiplex,
    multiply,
    multiply_,
    nan_to_num,
    nan_to_num_,
    nanmean,
    nansum,
    neg,
    neg_,
    nextafter,
    outer,
    polygamma,
    polygamma_,
    pow,
    pow_,
    prod,
    rad2deg,
    reciprocal,
    reciprocal_,
    reduce_as,
    remainder,
    remainder_,
    renorm,
    renorm_,
    round,
    round_,
    rsqrt,
    rsqrt_,
    scale,
    scale_,
    sgn,
    sigmoid,
    sigmoid_,
    sign,
    signbit,
    sin,
    sin_,
    sinc,
    sinc_,
    sinh,
    sinh_,
    sqrt,
    sqrt_,
    square,
    stanh,
    subtract,
    subtract_,
    sum,
    take,
    tan,
    tan_,
    tanh,
    tanh_,
    trace,
    trapezoid,
    trunc,
    trunc_,
    vander,
)
from .random import (  # noqa: F401
    bernoulli_,
    binomial,
    exponential_,
    log_normal,
    log_normal_,
    multinomial,
    normal,
    normal_,
    poisson,
    rand,
    randint,
    randint_like,
    randn,
    randperm,
    standard_normal,
    uniform,
    uniform_,
)
from .search import (  # noqa: F401
    argmax,
    argmin,
    argsort,
    bucketize,
    index_sample,
    index_select,
    kthvalue,
    masked_select,
    mode,
    nonzero,
    searchsorted,
    sort,
    top_p_sampling,
    topk,
    where,
    where_,
)
from .stat import (  # noqa: F401
    mean,
    median,
    nanmedian,
    nanquantile,
    numel,
    quantile,
    std,
    var,
)
from .to_string import set_printoptions  # noqa: F401

# this list used in math_op_patch.py for _binary_creator_
tensor_method_func = [
    'create_parameter',
    'create_tensor',
    'ormqr',
    'matmul',
    'dot',
    'cov',
    'corrcoef',
    'norm',
    'cond',
    'transpose',
    'cauchy_',
    'geometric_',
    'lstsq',
    'dist',
    't',
    't_',
    'cross',
    'cholesky',
    'cholesky_inverse',
    'bmm',
    'histogram',
    'histogram_bin_edges',
    'histogramdd',
    'bincount',
    'mv',
    'matrix_power',
    'qr',
    'householder_product',
    'pca_lowrank',
    'svd_lowrank',
    'eigvals',
    'eigvalsh',
    'abs',
    'acos',
    'all',
    'any',
    'asin',
    'asin_',
    'atan',
    'ceil',
    'ceil_',
    'cos',
    'cosh',
    'cumsum',
    'cumsum_',
    'cummax',
    'cummin',
    'cumprod',
    'cumprod_',
    'logcumsumexp',
    'logit',
    'logit_',
    'exp',
    'exp_',
    'expm1',
    'floor',
    'floor_',
    'increment',
    'logaddexp',
    'log',
    'log_',
    'log2',
    'log2_',
    'log10',
    'log10_',
    'logsumexp',
    'multiplex',
    'pow',
    'pow_',
    'prod',
    'reciprocal',
    'reciprocal_',
    'round',
    'round_',
    'rsqrt',
    'rsqrt_',
    'scale',
    'scale_',
    'sign',
    'sin',
    'sinc',
    'sinh',
    'sqrt',
    'sqrt_',
    'square',
    'stanh',
    'sum',
    'reduce_as',
    'multigammaln',
    'multigammaln_',
    'nan_to_num',
    'nan_to_num_',
    'hypot',
    'hypot_',
    'nansum',
    'nanmean',
    'block_diag',
    'count_nonzero',
    'tanh',
    'tanh_',
    'add_n',
    'max',
    'amax',
    'maximum',
    'min',
    'amin',
    'minimum',
    'fmax',
    'fmin',
    'mm',
    'inner',
    'outer',
    'divide',
    'divide_',
    'floor_divide',
    'floor_divide_',
    'remainder',
    'remainder_',
    'mod',
    'mod_',
    'floor_mod',
    'floor_mod_',
    'multiply',
    'multiply_',
    'add',
    'add_',
    'subtract',
    'subtract_',
    'inverse',
    'log1p',
    'log1p_',
    'erf',
    'addmm',
    'addmm_',
    'clip',
    'clip_',
    'trace',
    'kron',
    'kthvalue',
    'isfinite',
    'isin',
    'isinf',
    'isnan',
    'isneginf',
    'isposinf',
    'isreal',
    'broadcast_shape',
    'conj',
    'neg',
    'neg_',
    'lgamma',
    'lgamma_',
    'gammaincc',
    'gammaincc_',
    'gammainc',
    'gammainc_',
    'equal',
    'equal_',
    'equal_all',
    'greater_equal',
    'greater_equal_',
    'greater_than',
    'greater_than_',
    'is_empty',
    'less_equal',
    'less_equal_',
    'less_than',
    'less_than_',
    'logical_and',
    'logical_and_',
    'logical_not',
    'logical_not_',
    'logical_or',
    'logical_or_',
    'logical_xor',
    'logical_xor_',
    'not_equal',
    'not_equal_',
    'allclose',
    'isclose',
    'is_tensor',
    'cast',
    'cast_',
    'concat',
    'expand',
    'broadcast_to',
    'expand_as',
    'flatten',
    'flatten_',
    'gather',
    'gather_nd',
    'reshape',
    'reshape_',
    'reverse',
    'scatter',
    'scatter_',
    'scatter_nd_add',
    'scatter_nd',
    'shard_index',
    'slice',
    'slice_scatter',
    'split',
    'tensor_split',
    'hsplit',
    'dsplit',
    'vsplit',
    'chunk',
    'tensordot',
    'squeeze',
    'squeeze_',
    'stack',
    'strided_slice',
    'transpose',
    'transpose_',
    'cauchy_',
    'geometric_',
    'tan_',
    'unique',
    'unique_consecutive',
    'unsqueeze',
    'unsqueeze_',
    'unstack',
    'flip',
    'rot90',
    'unbind',
    'roll',
    'tile',
    'argmax',
    'argmin',
    'argsort',
    'masked_select',
    'topk',
    'top_p_sampling',
    'where',
    'where_',
    'index_select',
    'nonzero',
    'sort',
    'index_sample',
    'mean',
    'std',
    'var',
    'numel',
    'median',
    'nanmedian',
    'quantile',
    'nanquantile',
    'is_complex',
    'is_integer',
    'rank',
    'shape',
    'real',
    'imag',
    'is_floating_point',
    'gammaln',
    'gammaln_',
    'digamma',
    'digamma_',
    'diagonal',
    'trunc',
    'trunc_',
    'frac',
    'frac_',
    'bitwise_and',
    'bitwise_and_',
    'bitwise_or',
    'bitwise_or_',
    'bitwise_xor',
    'bitwise_xor_',
    'bitwise_not',
    'bitwise_not_',
    'broadcast_tensors',
    'eig',
    'uniform_',
    'multi_dot',
    'solve',
    'cholesky_solve',
    'triangular_solve',
    'asinh',
    'atanh',
    'atanh_',
    'acosh',
    'lu',
    'lu_unpack',
    'cdist',
    'as_complex',
    'as_real',
    'rad2deg',
    'deg2rad',
    'gcd',
    'gcd_',
    'lcm',
    'lcm_',
    'diff',
    "mode",
    'lerp',
    'lerp_',
    'erfinv',
    'erfinv_',
    'angle',
    'moveaxis',
    'repeat_interleave',
    'take_along_axis',
    'put_along_axis',
    'select_scatter',
    'put_along_axis_',
    'bernoulli_',
    'exponential_',
    'heaviside',
    'index_add',
    "index_add_",
    'index_put',
    'index_put_',
    'take',
    'bucketize',
    'sgn',
    'frexp',
    'ldexp',
    'ldexp_',
    'trapezoid',
    'cumulative_trapezoid',
    'polar',
    'sigmoid',
    'sigmoid_',
    'vander',
    'nextafter',
    'unflatten',
    'as_strided',
    'view',
    'view_as',
    'unfold',
    'i0',
    'i0_',
    'i0e',
    'i1',
    'i1e',
    'polygamma',
    'polygamma_',
    'masked_fill',
    'masked_fill_',
    'diag_embed',
    'atan2',
    'diagflat',
    'multinomial',
    'pinv',
    'renorm',
    'renorm_',
    'tan',
    'tan_',
    'tril',
    'tril_',
    'triu',
    'triu_',
    'stft',
    'istft',
    'abs_',
    'acos_',
    'atan_',
    'cos_',
    'cosh_',
    'sin_',
    'sinc_',
    'sinh_',
    'acosh_',
    'asinh_',
    'diag',
    'normal_',
    'copysign',
    'copysign_',
    'normal_',
    'bitwise_left_shift',
    'bitwise_left_shift_',
    'bitwise_right_shift',
    'bitwise_right_shift_',
    'index_fill',
    'index_fill_',
    'atleast_1d',
    'atleast_2d',
    'atleast_3d',
    'diagonal_scatter',
    'masked_scatter',
    'masked_scatter_',
    "combinations",
    'signbit',
    'log_normal_',
    'ser_',
]

# this list used in math_op_patch.py for magic_method bind
magic_method_func = [
    ('__and__', 'bitwise_and'),
    ('__or__', 'bitwise_or'),
    ('__xor__', 'bitwise_xor'),
    ('__invert__', 'bitwise_not'),
]
