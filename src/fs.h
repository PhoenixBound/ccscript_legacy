#pragma once
#ifdef _WIN32
	#include <filesystem>
	namespace fs = std::filesystem;
#else
	#include "filesystem/filesystem_mini.h"
	namespace fs = filesystem;
#endif
