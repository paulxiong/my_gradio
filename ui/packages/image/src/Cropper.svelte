<script lang="ts">
	import Cropper from "cropperjs";
	import { onMount, createEventDispatcher } from "svelte";

	export let image: string;
	export let crop_xy='boost init crop_xxy';
	let el: HTMLImageElement;


	const dispatch = createEventDispatcher();

	onMount(() => {
		const cropper = new Cropper(el, {
			autoCropArea: 1,
			cropend() {
				const image_data = cropper.getCroppedCanvas().toDataURL();
				// const crop_xy_data=cropper.getCropBoxData().width.toString();
				const crop_xy_data=cropper.getCropBoxData();
				// alert("boostx, crop_xy_data:  " + crop_xy_data );
				// dispatch("crop_exy",crop_xy_data);
				// console.log("boostx,  image_data      " + image_data);
				// dispatch("crop", image_data);
				dispatch("crop", {
					// image:image_data,
					// we only send the bigger original image back. 
					 image:image,
					crop_xy:crop_xy_data
				});
			}
		});
		// console.log("boostx, image    " + image);
		// dispatch("crop", image);
		return () => {
			cropper.destroy();
		};
	});
</script>

<img src={image} bind:this={el} alt=""/>
<p>boostx : {crop_xy}</p> 
