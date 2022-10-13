<script lang="ts">
	import Cropper from "cropperjs";
	import { onMount, createEventDispatcher } from "svelte";

	export let image: string;
	export let crop_xy='boost init crop_xxy';
	let el: HTMLImageElement;


	const dispatch = createEventDispatcher();
// How to do the training crop for autoanno
// Getting the {image} + {x,y,w,h} of Canvas
// 1. Get Canvas Data 
// 2. Get Crop Box Data 
// 3. Set “Set Crop Box Data” by result of step 1
// 4. Get Cropped Canvas ==> {image} 
// 5. Get Data ==> {x, y, width, height}
// 6. Set “Set Crop Box Data” by result of step 2
// Getting the {image} + {x,y,w,h} of Crop Box
// 7. repeat #4 and #5 to get  {image} + {x,y,w,h} of Crop Box
// What we need for Saving image and it’s annotation:

// * Image showing in Canvas, done by above step 4
// * Corresponding coordinates of box
// 	* x = (x of #7.5 - x of #5) / w of #5
//  * y = (y of #7.5 - y of #5) / h of #5
//  * w = w of #7.5
//  * h = h of #7.5
	onMount(() => {
		const cropper = new Cropper(el, {
			autoCropArea: 1,
			cropend() {
				// const crop_xy_data=cropper.getData();
				// const crop_image_size=cropper.getImageData();
				//get the canvas position, size for setting cropped box
				const canvas_data = cropper.getCanvasData();
				const cropped_box_data = cropper.getCropBoxData();  //backup the crop box data
				cropper.setCropBoxData(canvas_data)
				//get the cropped image, not the size, 
				const canvas_image = cropper.getCroppedCanvas().toDataURL();
				const canvas_image_xywh = cropper.getData();
				cropper.setCropBoxData(cropped_box_data); 		//restore the crop box data
				const cropped_image = cropper.getCroppedCanvas().toDataURL();
				const crop_image_xywh = cropper.getData();
				// alert("boostx, crop_xy_data:  " + crop_xy_data );
				// dispatch("crop_exy",crop_xy_data);
				console.log("boostx, canvas_imge" );
				console.log(canvas_image);
				console.log("boostx,  canvas_image_xywh      ");
				console.log(canvas_image_xywh);
				console.log("boostx,  crop_image_xywh      ");
				console.log(crop_image_xywh);
				// dispatch("crop", image_data);
				dispatch("crop", {
					// image:image_data,
					// we only send the bigger original image back. 
					image_tmp:cropped_image,
					canvas_image_xywh_tmp:canvas_image_xywh,
					crop_image_xywh_tmp:crop_image_xywh
				});
			}
		});
		// console.log("boostx, image    " + image);
		dispatch("crop", image);
		return () => {
			cropper.destroy();
		};
	});
</script>

<img src={image} bind:this={el} alt=""/>
<p>boostx : {crop_xy}</p> 
