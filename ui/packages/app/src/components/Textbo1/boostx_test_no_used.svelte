<script>
	// import image_boost from "../../../../image/src/Image.svelte";

	let hovering;
    let crop_xy_val;

    function crop_xy() {
        crop_xy_val="123456"
        alert(" boostx_tests.svelte: "+crop_xy_val)
    }

	function enter() {
        crop_xy_val="123456"
		hovering = true;
	}

	function leave() {
        crop_xy_val="123456"
		hovering = false;
	}
</script>
<div on:edit={crop_xy}>
    <slot crop_xy_val={crop_xy_val}></slot>
</div>
<div on:mouseenter={enter} on:mouseleave={leave}>
	<slot crop_xy_val={crop_xy_val}></slot>
	<slot hovering={hovering}></slot>
</div>