<script>
	// import Cropper from "../../../../image/src/Image.svelte";
	import { crop_xy_store } from './stores.ts';

	let hovering;
    let crop_xy_val;

    function crop_xy() {
        // crop_xy_val="123456"
        alert(" boostx_tests.svelte: "+crop_xy_val)
    }

	function enter() {
        // crop_xy_val=123456;
		hovering = true;
		// count.update(n => n + 1);
		// crop_xy_store.update(n => crop_xy_val );

	}

	function leave() {
        // crop_xy_val="00000000";
		hovering = false;
	}
</script>
<!-- <Cropper   on:crop={crop_xy} /> -->
<!-- <h1>The count is {crop_xy_val}</h1> -->
<div on:mouseenter={enter} on:mouseleave={leave}>
	<!-- <slot crop_xy_val={crop_xy_val}></slot> -->
	<p> This is test: {crop_xy_val}</p>
	<slot hovering={hovering}></slot>
</div>
<div class="box">
	<slot></slot>
</div>
