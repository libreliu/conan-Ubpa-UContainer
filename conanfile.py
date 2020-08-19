from conans import ConanFile, CMake, tools

class UContainer(ConanFile):
    name = "UContainer"
    version = "0.0.6"
    license = "MIT"
    url = "https://github.com/Ubpa/UContainer"
    description = "Ubpa Container"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "patches/*"

    def source(self):
        self.run("git clone https://github.com/Ubpa/UContainer.git --branch 0.0.6 --depth 1")

        # TODO: find a elegent way of copying
        content = tools.load("patches/UbpaEssential.cmake")
        tools.save("UContainer/UbpaEssential.cmake", content)
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly

#         tools.replace_in_file("UContainer/CMakeLists.txt", "PROJECT(MyHello)",
#                               '''PROJECT(MyHello)
# include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
# conan_basic_setup()''')


        tools.replace_in_file("UContainer/CMakeLists.txt", "include(cmake/InitUCMake.cmake)", "")
        tools.replace_in_file("UContainer/CMakeLists.txt", "Ubpa_InitUCMake()", "")
        tools.replace_in_file("UContainer/CMakeLists.txt", "Ubpa_InitProject()", "include(UbpaEssential.cmake)")

        tools.replace_in_file("UContainer/CMakeLists.txt", 'Ubpa_Export(DIRECTORIES "include")', "")


    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="UContainer")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="UContainer/include")
        self.copy("*.inl", dst="include", src="UContainer/include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["UContainer_core"]