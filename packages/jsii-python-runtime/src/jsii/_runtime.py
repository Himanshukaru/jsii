import weakref
import os

import attr

from jsii import _reference_map
from jsii._compat import importlib_resources
from jsii._kernel import Kernel
from jsii.python import _ClassPropertyMeta


# Yea, a global here is kind of gross, however, there's not really a better way of
# handling this. Fundamentally this is a global value, since we can only reasonably
# have a single kernel active at any one time in a real program.
kernel = Kernel()


@attr.s(auto_attribs=True, frozen=True, slots=True)
class JSIIAssembly:

    name: str
    version: str
    module: str
    filename: str

    @classmethod
    def load(cls, *args, _kernel=kernel, **kwargs):
        # Our object here really just acts as a record for our JSIIAssembly, it doesn't
        # offer any functionality itself, besides this class method that will trigger
        # the loading of the given assembly in the JSII Kernel.
        assembly = cls(*args, **kwargs)

        # Actually load the assembly into the kernel, we're using the
        # importlib.resources API here isntead of manually constructing the path, in
        # the hopes that this will make JSII modules able to be used with zipimport
        # instead of only on the FS.
        with importlib_resources.path(
            f"{assembly.module}._jsii", assembly.filename
        ) as assembly_path:
            _kernel.load(assembly.name, assembly.version, os.fspath(assembly_path))

        # Give our record of the assembly back to the caller.
        return assembly


class JSIIMeta(_ClassPropertyMeta, type):
    def __new__(cls, name, bases, attrs, *, jsii_type):
        attrs["__jsii_type__"] = jsii_type

        obj = super().__new__(name, bases, attrs)

        _reference_map.register_type(obj.__jsii_type__, obj)

        return obj

    def __call__(cls, *args, **kwargs):
        # Create our object at the JS level.
        # TODO: Handle args/kwargs
        # TODO: Handle Overrides
        ref = kernel.create(cls, args=args)

        # Create our object at the Python level.
        obj = cls.__class__.from_reference(cls, ref, **kwargs)

        # Whenever the object we're creating gets garbage collected, then we want to
        # delete it from the JS runtime as well.
        # TODO: Figure out if this is *really* true, what happens if something goes
        #       out of scope at the Python level, but something is holding onto it
        #       at the JS level? What mechanics are in place for this if any?
        weakref.finalize(obj, kernel.delete, obj.__jsii_ref__)

        # Instatiate our object at the Python level.
        if isinstance(obj, cls):
            obj.__init__(**kwargs)

        return obj

    def from_reference(cls, ref, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)
        obj.__jsii_ref__ = ref

        _reference_map.register_reference(obj.__jsii_ref__.ref, obj)

        return obj
