
/* Code to register embedded modules for meta path based loading if any. */

#include <Python.h>

/* Use a hex version of our own to compare for versions. We do not care about pre-releases */
#if PY_MICRO_VERSION < 16
#define PYTHON_VERSION (PY_MAJOR_VERSION * 256 + PY_MINOR_VERSION * 16 + PY_MICRO_VERSION)
#else
#define PYTHON_VERSION (PY_MAJOR_VERSION * 256 + PY_MINOR_VERSION * 16 + 15)
#endif

#include "nuitka/constants_blob.h"

#include "nuitka/unfreezing.h"

/* Type bool */
#ifndef __cplusplus
#include "stdbool.h"
#endif

#if 1 > 0
static unsigned char *bytecode_data[1];
#else
static unsigned char **bytecode_data = NULL;
#endif

/* Table for lookup to find compiled or bytecode modules included in this
 * binary or module, or put along this binary as extension modules. We do
 * our own loading for each of these.
 */
extern PyObject *modulecode___main__(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_card(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_card_printer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_deck(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_deck_analyzer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_game(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_translation(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);

static struct Nuitka_MetaPathBasedLoaderEntry meta_path_loader_entries[] = {
    {"__main__", modulecode___main__, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, L"\103\72\134\125\163\145\162\163\134\141\137\163\150\151\134\120\171\143\150\141\162\155\120\162\157\152\145\143\164\163\134\114\145\163\163\117\162\115\157\162\145\103\141\162\144\134\155\141\151\156\56\160\171"
#endif
},
    {"card", modulecode_card, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, L"\103\72\134\125\163\145\162\163\134\141\137\163\150\151\134\120\171\143\150\141\162\155\120\162\157\152\145\143\164\163\134\114\145\163\163\117\162\115\157\162\145\103\141\162\144\134\143\141\162\144\56\160\171"
#endif
},
    {"card_printer", modulecode_card_printer, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, L"\103\72\134\125\163\145\162\163\134\141\137\163\150\151\134\120\171\143\150\141\162\155\120\162\157\152\145\143\164\163\134\114\145\163\163\117\162\115\157\162\145\103\141\162\144\134\143\141\162\144\137\160\162\151\156\164\145\162\56\160\171"
#endif
},
    {"deck", modulecode_deck, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, L"\103\72\134\125\163\145\162\163\134\141\137\163\150\151\134\120\171\143\150\141\162\155\120\162\157\152\145\143\164\163\134\114\145\163\163\117\162\115\157\162\145\103\141\162\144\134\144\145\143\153\56\160\171"
#endif
},
    {"deck_analyzer", modulecode_deck_analyzer, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, L"\103\72\134\125\163\145\162\163\134\141\137\163\150\151\134\120\171\143\150\141\162\155\120\162\157\152\145\143\164\163\134\114\145\163\163\117\162\115\157\162\145\103\141\162\144\134\144\145\143\153\137\141\156\141\154\171\172\145\162\56\160\171"
#endif
},
    {"game", modulecode_game, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, L"\103\72\134\125\163\145\162\163\134\141\137\163\150\151\134\120\171\143\150\141\162\155\120\162\157\152\145\143\164\163\134\114\145\163\163\117\162\115\157\162\145\103\141\162\144\134\147\141\155\145\56\160\171"
#endif
},
    {"site", NULL, 0, 29825, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, L"\103\72\134\120\162\157\147\162\141\155\40\106\151\154\145\163\134\120\171\164\150\157\156\63\61\61\134\114\151\142\134\163\151\164\145\56\160\171"
#endif
},
    {"translation", modulecode_translation, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, L"\103\72\134\125\163\145\162\163\134\141\137\163\150\151\134\120\171\143\150\141\162\155\120\162\157\152\145\143\164\163\134\114\145\163\163\117\162\115\157\162\145\103\141\162\144\134\164\162\141\156\163\154\141\164\151\157\156\56\160\171"
#endif
},
    {NULL, NULL, 0, 0, 0}
};

static void _loadBytesCodesBlob(void) {
    static bool init_done = false;

    if (init_done == false) {
        loadConstantsBlob((PyObject **)bytecode_data, ".bytecode");

        init_done = true;
    }
}


void setupMetaPathBasedLoader(void) {
    static bool init_done = false;
    if (init_done == false) {
        _loadBytesCodesBlob();
        registerMetaPathBasedUnfreezer(meta_path_loader_entries, bytecode_data);

        init_done = true;
    }
}

// This provides the frozen (compiled bytecode) files that are included if
// any.

// These modules should be loaded as bytecode. They may e.g. have to be loadable
// during "Py_Initialize" already, or for irrelevance, they are only included
// in this un-optimized form. These are not compiled by Nuitka, and therefore
// are not accelerated at all, merely bundled with the binary or module, so
// that CPython library can start out finding them.

struct frozen_desc {
    char const *name;
    int index;
    int size;
};

static struct frozen_desc _frozen_modules[] = {

    {NULL, 0, 0}
};


void copyFrozenModulesTo(struct _frozen *destination) {
    _loadBytesCodesBlob();

    struct frozen_desc *current = _frozen_modules;

    for (;;) {
        destination->name = (char *)current->name;
        destination->code = bytecode_data[current->index];
        destination->size = current->size;
#if PYTHON_VERSION >= 0x3b0
        destination->is_package = current->size < 0;
        destination->size = Py_ABS(destination->size);
        destination->get_code = NULL;
#endif
        if (destination->name == NULL) break;

        current += 1;
        destination += 1;
    };
}

