# -*- coding: utf-8 -*-

from cffi import FFI

MHASH_MD5 = 5

ffi = FFI()
ffi.cdef("""
typedef enum __hashid {
        MHASH_CRC32             =  0,
        MHASH_MD5               =  1,
        MHASH_SHA1              =  2,
        MHASH_HAVAL256          =  3,
        MHASH_RIPEMD160         =  5,
        MHASH_TIGER192          =  7,
        MHASH_GOST              =  8,
        MHASH_CRC32B            =  9,
        MHASH_HAVAL224          = 10,
        MHASH_HAVAL192          = 11,
        MHASH_HAVAL160          = 12,
        MHASH_HAVAL128          = 13,
        MHASH_TIGER128          = 14,
        MHASH_TIGER160          = 15,
        MHASH_MD4               = 16
} hashid;

typedef uint32_t mutils_word32;
typedef uint8_t mutils_word8;

typedef char mutils_boolean;

typedef void (*INIT_FUNC)( void*);
typedef void (*HASH_FUNC)(void*, const void*, int);
typedef void (*FINAL_FUNC)(void*);
typedef void (*DEINIT_FUNC)(void*, unsigned char*);

typedef struct __MHASH_INSTANCE
{
        mutils_word32 hmac_key_size;
        mutils_word32 hmac_block;
        mutils_word8 *hmac_key;

        mutils_word8 *state;
        mutils_word32 state_size;
        hashid algorithm_given;

        HASH_FUNC hash_func;
        FINAL_FUNC final_func;
        DEINIT_FUNC deinit_func;
} MHASH_INSTANCE;

typedef MHASH_INSTANCE *MHASH;



MHASH mhash_init(hashid type);
mutils_boolean mhash(MHASH thread, const void *plaintext, mutils_word32 size);
mutils_word32 mhash_get_block_size(hashid type);
void *mhash_end(MHASH thread);
""")

lib = ffi.dlopen("mhash")
