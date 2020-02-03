vec2 CalculateIds(float Melanin, float KB, float BloodSaturation, uint KEpi){
	float mel_min = 0.0;
	float mel_max = 0.1;
	float mel_step = 0.01;
	uint mel_steps = uint(int(mel_max/mel_step) + 1);

	float kb_min = 0.0;
	float kb_max = 2.0;
	float kb_step = 0.1;
	uint kb_steps = uint(int(kb_max/kb_step) + 1);

	float blood_min = 0.3;
	float blood_max = 1.0;
	float blood_step = 0.01;
	uint blood_steps = uint(int((blood_max - blood_min)/blood_step) + 1);

	float kepi_min = 1.0;
	float kepi_max = 5.0;
	float kepi_step = 1.0;
	uint kepi_steps = uint(int((kepi_max - kepi_min)/kepi_step) + 1);

	uint mel_steps_made = uint(int(round((Melanin - mel_min)/mel_step)));
	uint kb_steps_made = uint(int(round((KB - kb_min)/kb_step)));
	uint blood_steps_made = uint(int(round((BloodSaturation - blood_min)/blood_step)));
	uint kepi_steps_made = uint(int(round((float(KEpi) - kepi_min)/kepi_step)));

	int maxid = int(mel_steps * kb_steps * blood_steps * kepi_steps);

	uint id = (mel_steps_made * kb_steps * blood_steps * kepi_steps) 
				+ (kb_steps_made * blood_steps * kepi_steps) 
				+ (blood_steps_made * kepi_steps) 
				+ kepi_steps_made;

	return vec2(id, maxid);
}

vec2 FindUvs(vec2 ids) {
	uint img_dim = uint(int(ceil(sqrt(ids.y))));
	uint id = uint(int(ids.x));

	float ui = mod(float(id), float(img_dim));
	float vi = float(float(float(id) - float(ui))/float(img_dim));

	float u = ui / float(img_dim);
	float v = vi / float(img_dim);

	return vec2(u, v);
}

vec4 FindChromophores(sampler2D tex, float Melanin, float KB, float BloodSaturation, uint KEpi){
	vec2 ids = CalculateIds(Melanin, KB, BloodSaturation, KEpi);
	vec2 uv = FindUvs(ids);
	
	return texture(tex, uv);
}