from conan import ConanFile
import conan.tools.files
from conan.tools.cmake import CMake
import os


class GTESTConan(ConanFile):
    name = "gtest"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "CMakeToolchain"

    def export_sources(self):
        conan.tools.files.copy(self, "*", self.recipe_folder, self.export_sources_folder)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "none")
        self.cpp_info.builddirs.append(os.path.join("lib", "cmake"))
        self.cpp_info.set_property("cmake_file_name", "GTest")
