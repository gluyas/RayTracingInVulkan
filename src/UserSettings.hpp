#pragma once

struct UserSettings final
{
	// Application
	bool Benchmark;

	// Benchmark
	bool BenchmarkNextScenes{};
	uint32_t BenchmarkMaxTime{};
	
	// Scene
	int SceneIndex;

	// Renderer
	bool IsRayTraced;
	bool AccumulateRays;
	uint32_t NumberOfSamples;
	uint32_t NumberOfBounces;
	uint32_t MaxNumberOfSamples;

	// Camera
	float FieldOfView;
	float Aperture;
	float FocusDistance;
	bool GammaCorrection;

	// UI
	bool ShowSettings;
	bool ShowOverlay;

	// Scene
	bool RenderTextures;

	//Skin
	float Melanin;
	float KB;
	float BloodSaturation;
	int KEpi;

	bool RequiresAccumulationReset(const UserSettings& prev) const
	{
		return
			IsRayTraced != prev.IsRayTraced ||
			AccumulateRays != prev.AccumulateRays ||
			NumberOfBounces != prev.NumberOfBounces ||
			FieldOfView != prev.FieldOfView ||
			Aperture != prev.Aperture ||
			FocusDistance != prev.FocusDistance ||
			Melanin != prev.Melanin ||
			KB != prev.KB ||
			BloodSaturation != prev.BloodSaturation ||
			KEpi != prev.KEpi;
	}

	bool RequiresReload(const UserSettings& prev) const
	{
		return RenderTextures != prev.RenderTextures;
	}
};
